alf = 'aábcdeéfghiíjklmnñoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ0123456789 ,.:-()'
a = 8
b = 44
newAlf = ''

for letter in alf:
    newAlf += alf[(alf.index(letter)*a + b)%len(alf)]

text = 'fJ25bJ cbP Í4J252úi54úbú5áiJ54úÚÚÍci c5.c5JváJd55nÁÍ2 ci5.ÍñcÚ2J25 cúÚÓJ254úbI,Í4J.J2:5c254ÍcÚ ú:5IcÚú55,J5,BvÍ4J5WP2Í4J5c25báH52ci4Í,,Jd'
newtext = ''
for letter in text:
    newtext += alf[(newAlf.index(letter))]

print('Solucion : "' + newtext+ '"')