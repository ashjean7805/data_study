# Shell

## Definition
Shell(쉘)은 운영체제상에서 사용자가 입력하는 명령을 읽고 해석하여 대신 실행해주는 프로그램이다. 즉 다시말해서, 운영체제의 커널과 사용자 사이를 이어주는 역할을 하며 사용자의 명령어를 해석하고 운영체제가 알아들을 수 있도록 도와주는 명령어 해석기이다.

쉘은 Unix나 리눅스에만 있는 것이 아니라 Windows나 다른 운영체제에도 필수적으로 존재한다.


## 종류
bash : Bourne-Again Shell(프롬프트 : #, 경로 : /bin/bash). 가장 대표적으로 사용.

sh : Bourne Shell(프롬프트 : $, 경로 : /bin/sh)

csh : C Shell(프롬프트 : %, 경로 : /bin/csh)

tcsh : TENEX C Shell(프롬프트 : >, 경로 : /bin/tcsh)

ksh : Korn Shell(프롬프트 : $, 경로 : /bin/ksh)

zsh : Z shell(프롬프츠 : %, 경로 : /bin/zsh) : 경로 확인 필요 


## 환경변수
쉘은 여러가지 환경변수를 사용하는데 이 환경변수는 사용자가 임의로 값의 변경이 가능하다. 하지만 미리 정의된 환경변수의 이름을 변경해서는 안된다. 쉘의 종류에 따라 설정, 확인 방법이 다르다. 

쉘의 환경변수는 로그인 할 때 설정된다. 사용자 환경은 프로파일에서 설정되는데 프로파일은 글로벌 프로파일과 계정프로파일 두가지가 존재한다. 

# Shell Script
## Definition
Shell Script(쉘 스크립트)란 Shell(쉘)에서 사용할 수 있는 명령어들의 조합을 모아서 만든 배치(batch)파일이다.

스크립트(Script) : 일반적으로 인터프리트(interpret) 방식으로 동작하는 컴파일되지 않은 프로그램
 -> 프로그램의 한 라인을 읽어 해석하고 실행하는 과정을 반복하도록 만들어진, 프로그래밍 언어로 작성된, 컴파일되지 않은 파일에 저장된 프로그램
 -> 텍스트 형식으로 저장되는 프로그램, 한줄씩 순차적으로 읽어 실행되도록 작성된 프로그램
 
   즉, 운영체제의 Shell을 이용하여 한줄씩 순차적으로 읽으면서 명령어들을 실행시켜주는 인터프리터 방식의 프로그램이다. Shell Script를 활용하여 묶어진 명령어 조합을 수행하거나 반복적인 명령어를 단일 명령으로 쉽게 사용할 수 있다. 

## 기본 구조

### shebang

    !/bin/bash
    echo "Hello Shellscript!!"

shebang은 코드 첫 번째 줄을 지칭하는 말로 sharp(#) + bang(!)의 합성어이다. Unix 계열 shell script 파일의 필수적인 구문이다. Script 파일 최상단에 해당 파일을 해석해줄 인터프리터의 절대경로를 지정해주는 것이다. 위의 예시는 bash shell을 인터프리터로 지정한 것이다. 
                                                                              



# Reference
 https://blogger.pe.kr/300

https://blogger.pe.kr/320

https://minkwon4.tistory.com/159

https://thenicesj.tistory.com/209
