#!/usr/bin/env python3
"""
번역 품질 개선: 추가 오류 수정
- 철자 오류 (많운 → 많은)
- 조사 오류 (분가 → 분이, 뉘우침와 → 뉘우침과)
- 어색한 표현 (구해냄자 → 구원자, 구해주심자 → 구원자)
"""

import glob

# 수정 패턴 목록
REPLACEMENTS = [
    # 철자 오류
    ("많운 ", "많은 "),

    # 조사 오류
    ("분가 ", "분이 "),
    ("뉘우침와 ", "뉘우침과 "),

    # 어색한 표현 수정 (어린이가 이해하기 쉽게)
    ("구해냄자", "구원자"),
    ("구해주심자", "구원자"),
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
    print("번역 품질 개선: 추가 오류 수정")
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
