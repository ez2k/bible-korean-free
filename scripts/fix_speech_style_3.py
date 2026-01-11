#!/usr/bin/env python3
"""
어투 일관성 수정 스크립트 (3차)
추가 반말체/문어체 패턴 수정

수정 패턴:
- "~ㄴ다." → "~아요/어요."
- "~는다." → "~아요/어요."
"""

import glob
import re

def fix_speech_style_3():
    files = glob.glob('/root/bible-korean-free/korean/*.json')

    stats = {
        '않는다." → 않아요."': 0,
        '온다." → 와요."': 0,
        '간다." → 가요."': 0,
        '준다." → 줘요."': 0,
        '같다." → 같아요."': 0,
        '른다." → 라요."': 0,
        '든다." → 들어요."': 0,
        '난다." → 나요."': 0,
        '산다." → 살아요."': 0,
        '만든다." → 만들어요."': 0,
        '한다." → 해요."': 0,
        '낸다." → 내요."': 0,
        '선다." → 서요."': 0,
        '는다." → 어요." (기타)': 0,
    }

    modified_files = []

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. "~않는다." → "~않아요."
        count = len(re.findall(r'않는다\."', content))
        stats['않는다." → 않아요."'] += count
        content = content.replace('않는다."', '않아요."')

        # 2. "~온다." → "~와요."
        count = len(re.findall(r'온다\."', content))
        stats['온다." → 와요."'] += count
        content = content.replace('온다."', '와요."')

        # 3. "~간다." → "~가요."
        count = len(re.findall(r'간다\."', content))
        stats['간다." → 가요."'] += count
        content = content.replace('간다."', '가요."')

        # 4. "~준다." → "~줘요."
        count = len(re.findall(r'준다\."', content))
        stats['준다." → 줘요."'] += count
        content = content.replace('준다."', '줘요."')

        # 5. "~같다." → "~같아요."
        count = len(re.findall(r'같다\."', content))
        stats['같다." → 같아요."'] += count
        content = content.replace('같다."', '같아요."')

        # 6. "~른다." → "~라요." (부른다, 다른다 등)
        count = len(re.findall(r'른다\."', content))
        stats['른다." → 라요."'] += count
        content = content.replace('른다."', '라요."')

        # 7. "~든다." → "~들어요." (듣다, 든다 등)
        count = len(re.findall(r'든다\."', content))
        stats['든다." → 들어요."'] += count
        content = content.replace('든다."', '들어요."')

        # 8. "~난다." → "~나요."
        count = len(re.findall(r'난다\."', content))
        stats['난다." → 나요."'] += count
        content = content.replace('난다."', '나요."')

        # 9. "~산다." → "~살아요."
        count = len(re.findall(r'산다\."', content))
        stats['산다." → 살아요."'] += count
        content = content.replace('산다."', '살아요."')

        # 10. "~만든다." → "~만들어요."
        count = len(re.findall(r'만든다\."', content))
        stats['만든다." → 만들어요."'] += count
        content = content.replace('만든다."', '만들어요."')

        # 11. "~한다." → "~해요."
        count = len(re.findall(r'한다\."', content))
        stats['한다." → 해요."'] += count
        content = content.replace('한다."', '해요."')

        # 12. "~낸다." → "~내요."
        count = len(re.findall(r'낸다\."', content))
        stats['낸다." → 내요."'] += count
        content = content.replace('낸다."', '내요."')

        # 13. "~선다." → "~서요."
        count = len(re.findall(r'선다\."', content))
        stats['선다." → 서요."'] += count
        content = content.replace('선다."', '서요."')

        # 변경된 경우에만 저장
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(filepath.split('/')[-1])

    return stats, modified_files

if __name__ == '__main__':
    print("어투 일관성 수정 (3차) 시작...")
    print("추가 반말체/문어체 패턴 수정\n")

    stats, modified_files = fix_speech_style_3()

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
