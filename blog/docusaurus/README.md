# Docusaurus
# Installation
node.js 설치
- chocolatey 도 같이 설치하기
docusaurus 설치
- yarn으로 바꿔 설치하기 

# Github Pages

# Github Action


# Branch 

## Naming Rule
### 배포
- gh-pages
- main
### 기능 개발
코드 완성되면 dev로 병합 후 main에 병합
- dev
    - 기능 개발 종합 브랜치
- dev-${NAME}
    - 기능 개발 개인 브랜치
### 콘텐츠 작성
- cont-${NAME}
    - 콘텐츠 파일만을 편집하여 즉각 배포 


# Deployment
source branch(메인 브랜치), deploy branch(배포 브랜치) 두가지 개념
- docusaurus deploy
    - source branch -> deploy branch
    - clonve, build and commit at one time
## docusaurus.config.js setting


## Trigerring

Github Action
 
