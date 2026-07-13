#!/bin/bash

# ======= Post Request variables ======
name="Aarzoo Bansal"
email="aarzoo1701@gmail.com"
content="Test Timeline Post APIs on my Portfolio Website. $RANDOM"


# ======= Post Request =======
echo "Creating time line post with the following data..."
echo "name = $name"
echo "email = $email"
echo "content = $content"
printf "\n"

postResponse=$(curl  -sS -X POST http://127.0.0.1:5000/api/timeline_post \
			--data-urlencode "name=$name" \
			--data-urlencode "email=$email" \
			--data-urlencode "content=$content")

printf "\n"

echo "Post Response:"
echo "$postResponse"

printf "\n"


# ======= GET Request ========
echo "# ================================== #"
echo "Running GET command..."

printf "\n"

echo "Get Response:"

getResponse=$(curl -sS http://127.0.0.1:5000/api/timeline_post)

echo "$getResponse"


# ======== Checking the Response =========
responseData=$(echo "$getResponse" | jq '.timeline_posts[0]')

responseName=$(echo "$responseData" | jq -r '.name')
responseEmail=$(echo "$responseData" | jq -r '.email')
responseContent=$(echo "$responseData" | jq -r '.content')

printf "\n\n"
if [[ $responseName == "$name" && "$responseEmail" == "$email" && "$responseContent" == "$content" ]]; then
	echo "TEST PASSED"
else
	echo "TEST FAILED"
	echo "expected: $name / $email / $content"
	echo "got:      $responseName / $responseEmail / $responseContent"
	exit 1
fi
