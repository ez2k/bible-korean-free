#!/usr/bin/env python3
"""
어투 일관성 수정 스크립트 (5차)
남은 반말체/문어체 패턴 수정
"""

import glob
import re

def fix_speech_style_5():
    files = glob.glob('/root/bible-korean-free/korean/*.json')

    stats = {
        # 습니다 → 어요 남은 패턴
        '바랍니다." → 바라요."': 0,
        '드립니다." → 드려요."': 0,
        '맙시다." → 말아요."': 0,

        # 다 → 어요/아요 패턴
        '없다." → 없어요."': 0,
        '있다." → 있어요."': 0,
        '않다." → 않아요."': 0,
        '못한다." → 못해요."': 0,
        '된다." → 돼요."': 0,
        '민다." → 밀어요."': 0,
        '낫다." → 나아요."': 0,
        '크다." → 커요."': 0,
        '많다." → 많아요."': 0,
        '적다." → 적어요."': 0,
        '높다." → 높아요."': 0,
        '멀다." → 멀어요."': 0,

        # 특정 표현
        '안다." → 알아요."': 0,
        '모른다." → 몰라요."': 0,
        '된다." → 돼요."': 0,
    }

    modified_files = []

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 습니다 → 어요
        count = len(re.findall(r'바랍니다\."', content))
        stats['바랍니다." → 바라요."'] += count
        content = content.replace('바랍니다."', '바라요."')

        count = len(re.findall(r'드립니다\."', content))
        stats['드립니다." → 드려요."'] += count
        content = content.replace('드립니다."', '드려요."')

        count = len(re.findall(r'맙시다\."', content))
        stats['맙시다." → 말아요."'] += count
        content = content.replace('맙시다."', '말아요."')

        # 다 → 어요/아요
        count = len(re.findall(r'없다\."', content))
        stats['없다." → 없어요."'] += count
        content = content.replace('없다."', '없어요."')

        count = len(re.findall(r'있다\."', content))
        stats['있다." → 있어요."'] += count
        content = content.replace('있다."', '있어요."')

        count = len(re.findall(r'않다\."', content))
        stats['않다." → 않아요."'] += count
        content = content.replace('않다."', '않아요."')

        count = len(re.findall(r'못한다\."', content))
        stats['못한다." → 못해요."'] += count
        content = content.replace('못한다."', '못해요."')

        count = len(re.findall(r'된다\."', content))
        stats['된다." → 돼요."'] += count
        content = content.replace('된다."', '돼요."')

        count = len(re.findall(r'낫다\."', content))
        stats['낫다." → 나아요."'] += count
        content = content.replace('낫다."', '나아요."')

        count = len(re.findall(r'크다\."', content))
        stats['크다." → 커요."'] += count
        content = content.replace('크다."', '커요."')

        count = len(re.findall(r'많다\."', content))
        stats['많다." → 많아요."'] += count
        content = content.replace('많다."', '많아요."')

        count = len(re.findall(r'적다\."', content))
        stats['적다." → 적어요."'] += count
        content = content.replace('적다."', '적어요."')

        count = len(re.findall(r'높다\."', content))
        stats['높다." → 높아요."'] += count
        content = content.replace('높다."', '높아요."')

        count = len(re.findall(r'멀다\."', content))
        stats['멀다." → 멀어요."'] += count
        content = content.replace('멀다."', '멀어요."')

        count = len(re.findall(r'안다\."', content))
        stats['안다." → 알아요."'] += count
        content = content.replace('안다."', '알아요."')

        count = len(re.findall(r'모른다\."', content))
        stats['모른다." → 몰라요."'] += count
        content = content.replace('모른다."', '몰라요."')

        # 변경된 경우에만 저장
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(filepath.split('/')[-1])

    return stats, modified_files

if __name__ == '__main__':
    print("어투 일관성 수정 (5차) 시작...")
    print("남은 반말체/문어체 패턴 수정\n")

    stats, modified_files = fix_speech_style_5()

    print("수정 통계:")
    total = 0
    for pattern, count in stats.items():
        if count > 0:
            print(f"  {pattern}: {count}건")
            total += count
    print(f"  ─────────────────")
    print(f"  총계: {total}건")

    print(f"\n수정된 파일: {len(modified_files)}개")
    for f in sorted(modified_files):
        print(f"  - {f}")

    print("\n완료!")
