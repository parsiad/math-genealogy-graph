#!/usr/bin/env python

import argparse
import collections
import re
import requests

from bs4 import BeautifulSoup

PATTERN = re.compile(r'^id.php\?id=([0-9]+)$')

def make_math_genealogy_graph(uid):
    print(f'digraph g{uid} {{')
    q = collections.deque([uid])
    visited = set([uid])
    while len(q) > 0:
        curr_uid = q.popleft()
        r = requests.get(f'https://www.mathgenealogy.org/id.php?id={curr_uid}')
        soup = BeautifulSoup(r.text, 'html.parser')
        name = " ".join(soup.h2.text.strip().split())
        alt = soup.span.text
        print(f'    x{curr_uid} [label="{name}\\n{alt}"];')
        advisors = soup.find(lambda tag: tag.name == 'p' and 'Advisor' in tag.text).find_all('a')
        for advisor in advisors:
            href = advisor.attrs['href']
            next_uid, = PATTERN.match(href).groups()
            print(f'    x{curr_uid} -> x{next_uid};')
            if next_uid in visited:
                continue
            q.append(next_uid)
            visited.add(next_uid)
    print('}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Make a math genealogy graph')
    parser.add_argument(
        'uid',
        help=('Identifier from mathgenealogy.org (you can find this in the URL; '
              'e.g. https://www.mathgenealogy.org/id.php?id=227045)'),
        type=int,
    )
    args = parser.parse_args()
    make_math_genealogy_graph(args.uid)
