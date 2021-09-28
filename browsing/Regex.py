import re

def pidRe(pid):
    
    dictRe = {r"\xe1":"á",r"\xe9":"é",r"\xed":"í",r"\xf3":"ó"
    ,r"\xfa":"ú",r"\xe0":"à",r"\xe8":"è",r"\xec":"ì",r"\xf2":"ò"
    ,r"\xf9":"ù",r"\xe3":"ã",r"\xf1":"ñ",r"\xf5":"õ",r"\xe2":"â"
    ,r"\xea":"ê",r"\xee":"î",r"\xf4":"ô",r"\xfb":"û",r"\xe4":"ä"
    ,r"\xeb":"ë",r"\xef":"ï",r"\xf6":"ö",r"\xfc":"ü",r"\xff":"ÿ"
    ,r"\xe7":"ç",r"\x96":"-",r"\xc1":"Á",r"\xc9":"É",r"\xcd":"Í"
    ,r"\xd3":"Ó",r"\xda":"Ú",r"\xc0":"À",r"\xc8":"È",r"\xcc":"Ì"
    ,r"\xd2":"Ò",r"\xd9":"Ù",r"\xc3":"Ã",r"\xd5":"Õ",r"\xd1":"Ñ"
    ,r"\xc2":"Â",r"\xca":"Ê",r"\xce":"Î",r"\xd4":"Ô",r"\xdb":"Û"
    ,r"\xc4":"Ä",r"\xcb":"Ë",r"\xcf":"Ï",r"\xd6":"Ö",r"\xdc":"Ü"
    ,r"\xc7":"Ç",r"\xaa":"ª",r"\u2500":"─", r"\x97":"—", r"\x92":"'"}
    
    for k,v in dictRe.items():
        pid = re.sub(k, v, str(pid))
    return pid
