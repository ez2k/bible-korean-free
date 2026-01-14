#!/usr/bin/env python3
"""
번역 품질 개선: 조사 오류 및 중복 표현 수정
- "하나님 말씀 전하는 사람가" → "하나님 말씀 전하는 사람이"
- "하나님 말씀 전하는 사람와" → "하나님 말씀 전하는 사람과"
- "하나님 말씀 전하는 사람여서" → "하나님 말씀 전하는 사람이어서"
- "하나님 말씀 전하는 사람를" → "하나님 말씀 전하는 사람을"
- "여하나님 말씀 전하는 사람" → "여자 선지자"
- "하나님의 하나님" 중복 제거
"""

import glob
import json
import re

# 수정 패턴 목록
REPLACEMENTS = [
    # 조사 오류 수정 (받침 없는 명사에 맞는 조사)
    ("하나님 말씀 전하는 사람가 ", "하나님 말씀 전하는 사람이 "),
    ("하나님 말씀 전하는 사람가\"", "하나님 말씀 전하는 사람이\""),
    ("하나님 말씀 전하는 사람가.", "하나님 말씀 전하는 사람이."),
    ("하나님 말씀 전하는 사람가,", "하나님 말씀 전하는 사람이,"),
    ("하나님 말씀 전하는 사람와 ", "하나님 말씀 전하는 사람과 "),
    ("하나님 말씀 전하는 사람여서", "하나님 말씀 전하는 사람이어서"),
    ("하나님 말씀 전하는 사람를 ", "하나님 말씀 전하는 사람을 "),
    ("하나님 말씀 전하는 사람를\"", "하나님 말씀 전하는 사람을\""),

    # 여선지자 표현 수정
    ("여하나님 말씀 전하는 사람가", "여자 선지자가"),
    ("여하나님 말씀 전하는 사람 ", "여자 선지자 "),
    ("여하나님 말씀 전하는 사람에게", "여자 선지자에게"),

    # "하나님의 하나님" 중복 제거
    ("하나님의 하나님의 법", "하나님의 법"),
    ("하나님의 하나님을 믿는 사람", "하나님을 믿는 사람"),
    ("하나님의 하나님을 만나는 천막", "하나님을 만나는 천막"),
    ("하나님의 하나님 말씀 전하는 사람", "하나님의 선지자"),

    # "백성"이 잘못 치환된 오류 수정
    ("백하나님을 믿는 사람", "백성"),
]

def fix_file(filepath):
    """파일의 오류를 수정하고 수정 횟수를 반환"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    total_fixes = 0

    for old, new in REPLACEMENTS:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            total_fixes += count
            print(f"  {old[:30]}... → {new[:30]}... : {count}건")

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return total_fixes

    return 0

def main():
    files = glob.glob('../korean/*.json')
    total_files = 0
    total_fixes = 0

    print("=" * 60)
    print("번역 품질 개선: 조사 오류 및 중복 표현 수정")
    print("=" * 60)

    for filepath in sorted(files):
        fixes = fix_file(filepath)
        if fixes > 0:
            filename = filepath.split('/')[-1]
            print(f"\n[{filename}] {fixes}건 수정")
            total_files += 1
            total_fixes += fixes

    print("\n" + "=" * 60)
    print(f"총 {total_files}개 파일에서 {total_fixes}건 수정 완료")
    print("=" * 60)

if __name__ == '__main__':
    main()
