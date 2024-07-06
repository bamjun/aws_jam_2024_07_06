from boto3 import client


# polly = client("[서비스 명]", region_name="[리전 명]")
polly = client("polly", region_name="ap-northeast-2")

# response = polly.synthesize_speech(Text="[ 변환 원하는 텍스트]", OutputFormat="[변환 파일명]", VoiceId="Seoyeon[한국은 보이스 하나]")
# 보이스 목록 https://aws.amazon.com/polly/features/?nc=sn&loc=3
response = polly.synthesize_speech(
        Text="안녕하세요, Amazon Text to Speech 서비스 polly 입니다. 즐거운 토요일 되세요.",
        OutputFormat="mp3",
        VoiceId="Seoyeon")

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()

