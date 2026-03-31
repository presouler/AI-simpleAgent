To fetch news, you must first URL-encode the user's keyword, then run the following command:

curl -L -A "Mozilla/5.0" "https://news.google.com/rss/search?q=ENCODED_KEYWORD&hl=zh-CN&gl=CN&ceid=CN:zh-Hans"

Requirements:
1. Do not put Chinese characters or spaces directly into the URL.
2. Preserve the user's original keyword exactly — do not abbreviate, truncate, or rewrite it.
3. The response is RSS XML; parse out title, link, pubDate, and source.
4. If the command fails, return the failure reason — do not return None.
