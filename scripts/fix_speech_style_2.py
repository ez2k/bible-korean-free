#!/usr/bin/env python3
"""
어투 일관성 수정 스크립트 (2차)
추가 반말체 패턴 수정

수정 패턴:
- "~았다." → "~았어요."
- "~었다." → "~었어요."
- "~셨다." → "~셨어요."
- "~렀다." → "~렀어요."
- "~ㅆ다." → "~ㅆ어요."
"""

import glob
import re

def fix_speech_style_2():
    files = glob.glob('/root/bible-korean-free/korean/*.json')

    stats = {
        '았다." → 았어요."': 0,
        '었다." → 었어요."': 0,
        '셨다." → 셨어요."': 0,
        '렀다." → 렀어요."': 0,
        '왔다." → 왔어요."': 0,
        '갔다." → 갔어요."': 0,
        '났다." → 났어요."': 0,
        '섰다." → 섰어요."': 0,
        '졌다." → 졌어요."': 0,
    }

    modified_files = []

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. "~았다." → "~았어요."
        count = len(re.findall(r'았다\."', content))
        stats['았다." → 았어요."'] += count
        content = content.replace('았다."', '았어요."')

        # 2. "~었다." → "~었어요."
        count = len(re.findall(r'었다\."', content))
        stats['었다." → 었어요."'] += count
        content = content.replace('었다."', '었어요."')

        # 3. "~셨다." → "~셨어요."
        count = len(re.findall(r'셨다\."', content))
        stats['셨다." → 셨어요."'] += count
        content = content.replace('셨다."', '셨어요."')

        # 4. "~렀다." → "~렀어요."
        count = len(re.findall(r'렀다\."', content))
        stats['렀다." → 렀어요."'] += count
        content = content.replace('렀다."', '렀어요."')

        # 5. "~왔다." → "~왔어요."
        count = len(re.findall(r'왔다\."', content))
        stats['왔다." → 왔어요."'] += count
        content = content.replace('왔다."', '왔어요."')

        # 6. "~갔다." → "~갔어요."
        count = len(re.findall(r'갔다\."', content))
        stats['갔다." → 갔어요."'] += count
        content = content.replace('갔다."', '갔어요."')

        # 7. "~났다." → "~났어요."
        count = len(re.findall(r'났다\."', content))
        stats['났다." → 났어요."'] += count
        content = content.replace('났다."', '났어요."')

        # 8. "~섰다." → "~섰어요."
        count = len(re.findall(r'섰다\."', content))
        stats['섰다." → 섰어요."'] += count
        content = content.replace('섰다."', '섰어요."')

        # 9. "~졌다." → "~졌어요."
        count = len(re.findall(r'졌다\."', content))
        stats['졌다." → 졌어요."'] += count
        content = content.replace('졌다."', '졌어요."')

        # 변경된 경우에만 저장
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(filepath.split('/')[-1])

    return stats, modified_files

if __name__ == '__main__':
    print("어투 일관성 수정 (2차) 시작...")
    print("추가 반말체 패턴 수정\n")

    stats, modified_files = fix_speech_style_2()

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
