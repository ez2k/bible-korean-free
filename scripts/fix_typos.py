#!/usr/bin/env python3
"""
오타 수정 스크립트
- "하나님 하나님" → "하나님"
- "하나님는" → "하나님은"
- "하나님를" → "하나님을"
"""

import glob
import json

def fix_typos():
    files = glob.glob('/root/bible-korean-free/korean/*.json')

    stats = {
        '하나님 하나님': 0,
        '하나님는': 0,
        '하나님를': 0
    }

    modified_files = []

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 수정 전 카운트
        stats['하나님 하나님'] += content.count('하나님 하나님')
        stats['하나님는'] += content.count('하나님는')
        stats['하나님를'] += content.count('하나님를')

        # 수정 적용
        content = content.replace('하나님 하나님', '하나님')
        content = content.replace('하나님는', '하나님은')
        content = content.replace('하나님를', '하나님을')

        # 변경된 경우에만 저장
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(filepath.split('/')[-1])

    return stats, modified_files

if __name__ == '__main__':
    print("오타 수정 시작...")
    stats, modified_files = fix_typos()

    print("\n수정 통계:")
    for typo, count in stats.items():
        print(f"  '{typo}' → {count}건 수정")

    print(f"\n총 수정된 파일: {len(modified_files)}개")
    for f in modified_files:
        print(f"  - {f}")

    print("\n완료!")
