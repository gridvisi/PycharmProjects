
'''

PyCharm is an Integrated
Development Environment (IDE) designed
to maximize productivity. It provides
clever code completion, static code
analysis, and refactorings, and lets
you focus on the bright side of
software development making
it an enjoyable experience.

Default:
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
 0123456789 (){}[]
 +-*/= .,;:!? #&$%@|^

Bold:
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
 0123456789 (){}[]
 +-*/= .,;:!? #&$%@|^

<!-- -- != := === >= >- >=> |-> -> <$>
</> #[ |||> |= ~@
'''

from collections import defaultdict
data = """Tim,ID
Sara,BR
Thelma,CN
Chris,RU
Fina,ID
Juliana,SE
Roberto,CN
Mario,PL
Paul,CN"""
countries = defaultdict(list)
for line in data.splitlines():
    name,country_code = line.split(",")
    countries[country_code].append(name)
print(countries)