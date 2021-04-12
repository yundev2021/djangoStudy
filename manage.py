#!/usr/bin/env python

# env -> 환경 변수에서 지정한 언어의 위치를 찾아서 실행g한다.
# env 라고 치면 환경변수가 출력된다.

import os
import sys

def main():
    # dictionary ==> setdefault ==> 키값이 있다면 키값을 반환하고 없다면 두번째 인자를 반환 기본값으로 할당하고 그 값을 리턴한다.
    os.environ.setdefault('DJANGO_SETTING_MODULE', 'DEV11.settings')
    #print(os.environ) #시스템 환경변수 출력, HONE 디렉토리, PATH 따위
    
    try:
        from mydjango import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Import Error") from exc
    execute_from_command_line()


if __name__ == '__main__':
    main()

	