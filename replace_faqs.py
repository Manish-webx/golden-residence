import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('faqs.html', 'r', encoding='utf-8') as f:
    faqs_content = f.read()

pattern = r'(<div class="faq-list">).*?(      </div>\n    </div>\n  </section>)'

match = re.search(pattern, html, flags=re.DOTALL)
if match:
    print('Pattern matched!')
    html_new = html[:match.start(1)] + '<div class="faq-list">\n' + faqs_content + match.group(2) + html[match.end(2):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_new)
else:
    print('Pattern did not match!')
