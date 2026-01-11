#!/usr/bin/env python3
"""
어투 일관성 수정 스크립트 (4차)
습니다 → 어요 변환 및 추가 패턴 수정
"""

import glob
import re

def fix_speech_style_4():
    files = glob.glob('/root/bible-korean-free/korean/*.json')

    stats = {
        '했습니다." → 했어요."': 0,
        '습니다." → 어요."': 0,
        '겠습니다." → 겠어요."': 0,
        '았습니다." → 았어요."': 0,
        '었습니다." → 었어요."': 0,
        '셨습니다." → 셨어요."': 0,
        '렸습니다." → 렸어요."': 0,
        '졌습니다." → 졌어요."': 0,
        '씁니다." → 써요."': 0,
        '랍니다." → 라요."': 0,
        '압니다." → 알아요."': 0,
        '맙시다." → 말아요."': 0,
        '쳤다." → 쳤어요."': 0,
        '렸다." → 렸어요."': 0,
        '린다." → 려요."': 0,
        '진다." → 져요."': 0,
        '친다." → 쳐요."': 0,
        '킨다." → 켜요."': 0,
    }

    modified_files = []

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 습니다 패턴들 (순서 중요: 특수 패턴 먼저)
        # 1. "~했습니다." → "~했어요."
        count = len(re.findall(r'했습니다\."', content))
        stats['했습니다." → 했어요."'] += count
        content = content.replace('했습니다."', '했어요."')

        # 2. "~겠습니다." → "~겠어요."
        count = len(re.findall(r'겠습니다\."', content))
        stats['겠습니다." → 겠어요."'] += count
        content = content.replace('겠습니다."', '겠어요."')

        # 3. "~았습니다." → "~았어요."
        count = len(re.findall(r'았습니다\."', content))
        stats['았습니다." → 았어요."'] += count
        content = content.replace('았습니다."', '았어요."')

        # 4. "~었습니다." → "~었어요."
        count = len(re.findall(r'었습니다\."', content))
        stats['었습니다." → 었어요."'] += count
        content = content.replace('었습니다."', '었어요."')

        # 5. "~셨습니다." → "~셨어요."
        count = len(re.findall(r'셨습니다\."', content))
        stats['셨습니다." → 셨어요."'] += count
        content = content.replace('셨습니다."', '셨어요."')

        # 6. "~습니다." → "~어요." (남은 일반 패턴)
        count = len(re.findall(r'습니다\."', content))
        stats['습니다." → 어요."'] += count
        content = content.replace('습니다."', '어요."')

        # 추가 패턴들
        # 6. "~쳤다." → "~쳤어요."
        count = len(re.findall(r'쳤다\."', content))
        stats['쳤다." → 쳤어요."'] += count
        content = content.replace('쳤다."', '쳤어요."')

        # 7. "~렸다." → "~렸어요."
        count = len(re.findall(r'렸다\."', content))
        stats['렸다." → 렸어요."'] += count
        content = content.replace('렸다."', '렸어요."')

        # 8. "~린다." → "~려요."
        count = len(re.findall(r'린다\."', content))
        stats['린다." → 려요."'] += count
        content = content.replace('린다."', '려요."')

        # 9. "~진다." → "~져요."
        count = len(re.findall(r'진다\."', content))
        stats['진다." → 져요."'] += count
        content = content.replace('진다."', '져요."')

        # 10. "~친다." → "~쳐요."
        count = len(re.findall(r'친다\."', content))
        stats['친다." → 쳐요."'] += count
        content = content.replace('친다."', '쳐요."')

        # 11. "~킨다." → "~켜요."
        count = len(re.findall(r'킨다\."', content))
        stats['킨다." → 켜요."'] += count
        content = content.replace('킨다."', '켜요."')

        # 변경된 경우에만 저장
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(filepath.split('/')[-1])

    return stats, modified_files

if __name__ == '__main__':
    print("어투 일관성 수정 (4차) 시작...")
    print("습니다 → 어요 변환 및 추가 패턴\n")

    stats, modified_files = fix_speech_style_4()

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
