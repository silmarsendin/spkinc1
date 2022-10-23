from asyncore import write
import streamlit as st
#from streamlit_option_menu import option_menu


from PIL import Image
image = Image.open('spkinc1.png')
st.image(image)
st.write('Aplicativo para auxiliar a identificar os parâmetros de cálculo do sistema de chuveiros automáticos em riscos gerais')
st.write('Este aplicativo não atende os riscos como depósitos, líquidos igníferos e demais riscos especiais')
#st.subheader('Escolha o tipo de bico.')
#select = option_menu(
    #menu_title=None,
    #options=["Spray Padrão", "Spray Est.","CCAE", "ESFR"],
    #icons=["caret-down","caret-down-square","caret-down-fill","caret-down-square-fill"],
    #menu_icon="cast",
    #default_index=0,
    #orientation="horizontal",
#)
select = st.sidebar.selectbox('Escolha o tipo de Bico',["Spray Padrão", "Spray Est.","CCAE", "ESFR"])

if select == "Spray Padrão":

    ocupacao = st.selectbox('Qual a ocupação:',['Escolha uma das ocupações da lista','aplicação de líquidos inflamáveis por spray pintura por flowcoating',
    'áreas de aplicação de resinas','áreas de serviço de restaurantes','áreas de usinagem','áreas de uso de fluidos hidráulicos combustíveis','asilos e casas de repouso',
    'bibliotecas – áreas de prateleiras altas','bibliotecas e salas de leituras, exceto salas com prateleiras altas','clubes','confeitarias','correios','destilarias',
    'edifícios residenciais e similares','escolas públicas e privadas (1, 2 e 3 graus)','estábulos','estacionamentos de veículos e showrooms','estofamento de móveis com espumas plásticas',
'extrusão de metais','fabricação de bebidas (refrigerantes, sucos)','fabricação de compensados e aglomerados','fabricação de pneus','fabricação de produtos de couro','fabricação de produtos de tabaco',
'fabricação de vidro e produtos de vidro','fábricas de conservas','fábricas de papel e celulose','fábricas de produtos eletrônicos','fábricas de produtos químicos – comuns','fábricas de ração animal',
'fundições','gráficas','gráficas [que utilizem tintas com ponto de fulgor menor que 100°F (38 °C)]','hangares','hospitais com ambulatórios','cirurgia e centros de saúde','hotéis','igrejas',
'indústria metalúrgica','indústrias têxteis','instalações para lavagem a seco','lavanderias','limpeza com solventes','lojas',
'manufatura de casas pré-fabricadas ou componentes pré-fabricados para construção (quando a estrutura final estiver presente e tiver interiores combustíveis)','moinhos de grãos','museus',
'oficinas mecânicas','padarias','palcos','píeres e embarcadouros','pintura e envernizamento por imersão','prédios da administração pública','prédios de escritórios, incluindo processamento de dados',
'áreas de refeição em restaurantes, exceto áreas de serviço','teatros e auditórios exceto palcos e proscênios','processamento de madeira montagem de produtos de madeira','processamento de papel',
'processamento de plásticos','processamento e fabricação de produtos lácteos','processos da indústria têxtil: escolha da matéria-prima, abertura de fardos, elaboração de misturas, batedores, cardagem etc.',
'recuperação, formulação, secagem, moagem e vulcanização de borracha','saturação com asfalto','serrarias','tratamento térmico em tanques de óleo abertos'])

#Risco Extaordinário - Grupo 2
    if ocupacao == 'aplicação de líquidos inflamáveis por spray pintura por flowcoating' or ocupacao == 'limpeza com solventes' or ocupacao == 'manufatura de casas pré-fabricadas ou componentes pré-fabricados para construção (quando a estrutura final estiver presente e tiver interiores combustíveis)' or ocupacao == 'pintura e envernizamento por imersão' or ocupacao == 'processamento de plásticos' or ocupacao == 'saturação com asfalto' or ocupacao == 'tratamento térmico em tanques de óleo abertos':
        st.write('Risco extraordinário – Grupo 2 de acordo com a Tabela A.1 da NBR 10.897/20.')
        areaop = st.select_slider(
        'Defina a área de operações:',
        options=['230', '240', '260', '280', '300', '320', '340','340','360','380','400','420','440','460','465'])
        if areaop == '230':
            densidade = 16.3
        elif areaop == '240':
            densidade = 16.1
        elif areaop == '260':
            densidade = 16.25
        elif areaop == '280':
            densidade = 15.4
        elif areaop == '300':
            densidade = 14.8
        elif areaop == '320':
            densidade = 14.6
        elif areaop == '340':
            densidade = 14.3
        elif areaop == '360':
            densidade = 14
        elif areaop == '380':
            densidade = 13.5
        elif areaop == '400':
            densidade = 13.3
        elif areaop == '420':
            densidade = 13
        elif areaop == '440':
            densidade = 12.6
        elif areaop == '460':
            densidade = 12.3
        elif areaop == '465':
            densidade = 12.2
        st.write('Distâncias válidas para projetos por cálculos hidráulicos, não é válido para projetos por tabelas.')
        st.write('Para uma área de operação de ', areaop, 'm2, teremos uma densidade de ', densidade, 'lpm/m2')
        entrebicos = st.number_input('Insira a distância entre bicos no mesmo ramal (m):',value = 1.80)
        if entrebicos > 3.70:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 3.70 m')
        if entrebicos < 1.8:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        entreramais = st.number_input('Insira a distância entre os ramais (m):',value = 1.80)
        if entreramais > 3.70:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 3.70 m')
        if entreramais < 1.80:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        areabico = entrebicos * entreramais
        if areabico > 9.3:
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área não pode ser maior que 9,3 m2')
        areabicor = round(areabico,2)
        areaopc = int(areaop)    
        numerobico = areaopc / areabico
        vazaobico = densidade * entrebicos * entreramais
        vazaobicor = round(vazaobico,2)
        numerobicos = round(numerobico)
        st.write('A vazão mínima no bico mais desfavorável é de ', vazaobicor ,'lpm.')
        st.write('Considerando que cada bico cobre uma área de ', areabicor, 'm2, teremos ', numerobicos, 'bicos a serem calculados.')
        st.caption('Estas informações são válidas para bicos tipo spray de cobertura padrão, para os demais bicos mude o tipo de bico no menu lateral.')
        alturateto = st.radio(
        'Escolha a faixa de altura do telhado',
        options=['Até 6,1 m','> 6,1 m e <= 9,00 m', '> 9,00 m e <= 18,00 m'])
        if alturateto == 'Até 6,1 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 80','Fator K 115','Fator K 160'])
            if fatork == 'Fator K 80':
                pressaobico = (vazaobico / 80) * (vazaobico / 80)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 80 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)

                st.write('Para o fator K de 80, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada é de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
        elif alturateto == '> 6,1 m e <= 9,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 160','Fator K 200'])
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 200':
                pressaobico = (vazaobico / 200) * (vazaobico / 200)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 200 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico está vazão ira aumentar.')
        elif alturateto == '> 9,00 m e <= 18,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 160','Fator K 200'])
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
            elif fatork == 'Fator K 200':
                pressaobico = (vazaobico / 200) * (vazaobico / 200)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 200 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')

    #Risco Extaordinário - Grupo 1
    elif ocupacao == 'áreas de uso de fluidos hidráulicos combustíveis' or ocupacao == 'estofamento de móveis com espumas plásticas' or ocupacao == 'extrusão de metais' or ocupacao == 'fabricação de compensados e aglomerados' or ocupacao == 'fundições' or ocupacao == 'gráficas [que utilizem tintas com ponto de fulgor menor que 100°F (38 °C)]' or ocupacao == 'hangares' or ocupacao == 'processos da indústria têxtil: escolha da matéria-prima, abertura de fardos, elaboração de misturas, batedores, cardagem etc.' or ocupacao == 'serrarias' or ocupacao == 'recuperação, formulação, secagem, moagem e vulcanização de borracha':
        st.write('Risco extraordinário – Grupo 1 de acordo com a Tabela A.1 da NBR 10.897/20.')
        areaop = st.select_slider(
        'Defina a área de operações:',
        options=['230', '240', '260', '280', '300', '320', '340','340','360','380','400','420','440','460','465'])
        if areaop == '230':
            densidade = 12.2
        elif areaop == '240':
            densidade = 11.93
        elif areaop == '260':
            densidade = 11.66
        elif areaop == '280':
            densidade = 11.39
        elif areaop == '300':
            densidade = 11.12
        elif areaop == '320':
            densidade = 10.85
        elif areaop == '340':
            densidade = 10.58
        elif areaop == '360':
            densidade = 10.31
        elif areaop == '380':
            densidade = 10.04
        elif areaop == '400':
            densidade = 9.77
        elif areaop == '420':
            densidade = 9.5
        elif areaop == '440':
            densidade = 9.23
        elif areaop == '460':
            densidade = 8.70
        elif areaop == '465':
            densidade = 8.1
        st.write('Distâncias válidas para projetos por cálculos hidráulicos, não é válido para projetos por tabelas.')
        st.write('Para uma área de operação de ', areaop, 'm2, teremos uma densidade de ', densidade, 'lpm/m2')
        entrebicos = st.number_input('Insira a distância entre bicos no mesmo ramal (m):',value = 1.80)
        if entrebicos > 3.70 and densidade >= 10.2:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 3.70 m')
        elif entrebicos > 4.6 and densidade < 10.2:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 4.60 m')
        if entrebicos < 1.8:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        entreramais = st.number_input('Insira a distância entre os ramais (m):',value = 1.80)
        if entreramais > 3.70 and densidade >= 10.2:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 3.70 m')
        elif entreramais > 4.6 and densidade < 10.2:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 4.60 m')
        if entreramais < 1.80:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        areabico = entrebicos * entreramais
        if areabico > 9.3 and densidade >= 10.2:
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área não pode ser maior que 9,3 m2')
        elif areabico > 12.1 and densidade < 10.2:
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área não pode ser maior que 12.1 m2')
        areabicor = round(areabico,2)
        areaopc = int(areaop)    
        numerobico = areaopc / areabico
        vazaobico = densidade * entrebicos * entreramais
        vazaobicor = round(vazaobico,2)
        numerobicos = round(numerobico)
        st.write('A vazão mínima no bico mais desfavorável é de ', vazaobicor ,'lpm.')
        st.write('Considerando que cada bico cobre uma área de ', areabicor, 'm2, teremos ', numerobicos, 'bicos a serem calculados.')
        st.caption('Estas informações são válidas para bicos tipo spray de cobertura padrão, para os demais bicos mude o tipo de bico no menu lateral.')
        alturateto = st.radio(
        'Escolha a faixa de altura do telhado',
        options=['Até 6,1 m','> 6,1 m e <= 9,00 m', '> 9,00 m e <= 18,00 m'])
        if alturateto == 'Até 6,1 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 80','Fator K 115','Fator K 160'])
            if fatork == 'Fator K 80':
                pressaobico = (vazaobico / 80) * (vazaobico / 80)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 80 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 80, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico está vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
            elif fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
        elif alturateto == '> 6,1 m e <= 9,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 160','Fator K 200'])
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 200':
                pressaobico = (vazaobico / 200) * (vazaobico / 200)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 200 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
        elif alturateto == '> 9,00 m e <= 18,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 160','Fator K 200'])
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
            pressaobicor = round(pressaobico,2)
            st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
            vazaototal = vazaobicor * numerobico
            vazaototalr = round(vazaototal,2)
            st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')

        elif fatork == 'Fator K 200':
            pressaobico = (vazaobico / 200) * (vazaobico / 200)
            if pressaobico < 0.5:
                pressaobico = 0.5
                vazaobico = 200 * 0.707106781187
                vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 3.700 m2')
                reserva = (vazaototalr + 1900) * 90
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 1.900 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 90 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
    
    #Risco Ordinário - Grupo 2
    if ocupacao == 'áreas de aplicação de resinas' or ocupacao == 'áreas de usinagem' or ocupacao == 'bibliotecas – áreas de prateleiras altas' or ocupacao == 'confeitarias' or ocupacao == 'correios' or ocupacao == 'destilarias' or ocupacao == 'estábulos' or ocupacao == 'fabricação de pneus' or ocupacao == 'fabricação de produtos de couro' or ocupacao =='fabricação de produtos de tabaco' or ocupacao == 'fábricas de papel e celulose' or ocupacao == 'fábricas de produtos químicos – comuns' or ocupacao == 'fábricas de ração animal' or ocupacao == 'gráficas' or ocupacao == 'indústria metalúrgica' or ocupacao == 'indústrias têxteis' or ocupacao == 'instalações para lavagem a seco' or ocupacao == 'lojas' or ocupacao == 'moinhos de grãos' or ocupacao == 'oficinas mecânicas' or ocupacao == 'palcos' or ocupacao == 'píeres e embarcadouros' or ocupacao == 'processamento de madeira montagem de produtos de madeira' or ocupacao == 'processamento de papel':
        st.write('Risco Ordinário – Grupo 2 de acordo com a Tabela A.1 da NBR 10.897/20.')
        areaop = st.select_slider(
        'Defina a área de operações:',
        options=['140', '160', '180', '200', '220', '240', '260','280','300','320','340','360','370'])
        if areaop == '140':
            densidade = 8.1
        elif areaop == '160':
            densidade = 7.95
        elif areaop == '180':
            densidade = 7.8
        elif areaop == '200':
            densidade = 7.65
        elif areaop == '220':
            densidade = 7.5
        elif areaop == '240':
            densidade = 7.35
        elif areaop == '260':
            densidade = 7.2
        elif areaop == '280':
            densidade = 7.05
        elif areaop == '300':
            densidade = 6.9
        elif areaop == '320':
            densidade = 6.75
        elif areaop == '340':
            densidade = 6.6
        elif areaop == '360':
            densidade = 6.4
        elif areaop == '370':
            densidade = 6.1
    
        st.write('Para uma área de operação de ', areaop, 'm2, teremos uma densidade de ', densidade, 'lpm/m2')
        entrebicos = st.number_input('Insira a distância entre bicos no mesmo ramal (m):',value = 1.80)
        if entrebicos > 4.60:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 4.60 m')
        if entrebicos < 1.8:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        entreramais = st.number_input('Insira a distância entre os ramais (m):',value = 1.80)
        if entreramais > 4.60:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 4.60 m')
        if entreramais < 1.80:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        areabico = entrebicos * entreramais
        if areabico > 12.1:
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área não pode ser maior que 12.1 m2')
        areabicor = round(areabico,2)
        areaopc = int(areaop)    
        numerobico = areaopc / areabico
        vazaobico = densidade * entrebicos * entreramais
        vazaobicor = round(vazaobico,2)
        numerobicos = round(numerobico)
        st.write('A vazão mínima no bico mais desfavorável é de ', vazaobicor ,'lpm.')
        st.write('Considerando que cada bico cobre uma área de ', areabicor, 'm2, teremos ', numerobicos, 'bicos a serem calculados.')
        st.caption('Estas informações são válidas para bicos tipo spray de cobertura padrão, para os demais bicos mude o tipo de bico no menu lateral.')
        alturateto = st.radio(
        'Escolha a faixa de altura do telhado',
        options=['Até 6,1 m','> 6,1 m e <= 9,00 m', '> 9,00 m e <= 18,00 m'])
        if alturateto == 'Até 6,1 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 80','Fator K 115','Fator K 160'])
            if fatork == 'Fator K 80':
                pressaobico = (vazaobico / 80) * (vazaobico / 80)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 80 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)

                st.write('Para o fator K de 80, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada é de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
        elif alturateto == '> 6,1 m e <= 9,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 115','Fator K 160','Fator K 200'])
            if fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 200':
                pressaobico = (vazaobico / 200) * (vazaobico / 200)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 200 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico está vazão ira aumentar.')
        elif alturateto == '> 9,00 m e <= 18,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 115', 'Fator K 160','Fator K 200'])
            if fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
           
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 200':
                pressaobico = (vazaobico / 200) * (vazaobico / 200)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 200 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
       
    #Risco Ordinário - Grupo 1
    if ocupacao == 'áreas de serviço de restaurantes' or ocupacao == 'estacionamentos de veículos e showrooms' or ocupacao == 'fabricação de bebidas (refrigerantes, sucos)' or ocupacao == 'fabricação de vidro e produtos de vidro' or ocupacao == 'fábricas de conservas' or ocupacao == 'fábricas de produtos eletrônicos' or ocupacao == 'lavanderias' or ocupacao == 'padarias' or ocupacao == 'processamento e fabricação de produtos lácteos':
        st.write('Risco Ordinário – Grupo 1 de acordo com a Tabela A.1 da NBR 10.897/20.')
        areaop = st.select_slider(
        'Defina a área de operações:',
        options=['140', '160', '180', '200', '220', '240', '260','280','300','320','340','360','370'])
        if areaop == '140':
            densidade = 6.1
        elif areaop == '160':
            densidade = 5.95
        elif areaop == '180':
            densidade = 5.8
        elif areaop == '200':
            densidade = 5.65
        elif areaop == '220':
            densidade = 5.5
        elif areaop == '240':
            densidade = 5.35
        elif areaop == '260':
            densidade = 5.2
        elif areaop == '280':
            densidade = 5.05
        elif areaop == '300':
            densidade = 4.9
        elif areaop == '320':
            densidade = 4.75
        elif areaop == '340':
            densidade = 4.6
        elif areaop == '360':
            densidade = 4.4
        elif areaop == '370':
            densidade = 4.1
    
        st.write('Para uma área de operação de ', areaop, 'm2, teremos uma densidade de ', densidade, 'lpm/m2')
        entrebicos = st.number_input('Insira a distância entre bicos no mesmo ramal (m):',value = 1.80)
        if entrebicos > 4.60:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 4.60 m')
        if entrebicos < 1.8:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        entreramais = st.number_input('Insira a distância entre os ramais (m):',value = 1.80)
        if entreramais > 4.60:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 4.60 m')
        if entreramais < 1.80:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        areabico = entrebicos * entreramais
        if areabico > 12.1:
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área não pode ser maior que 12.1 m2')
        areabicor = round(areabico,2)
        areaopc = int(areaop)    
        numerobico = areaopc / areabico
        vazaobico = densidade * entrebicos * entreramais
        vazaobicor = round(vazaobico,2)
        numerobicos = round(numerobico)
        st.write('A vazão mínima no bico mais desfavorável é de ', vazaobicor ,'lpm.')
        st.write('Considerando que cada bico cobre uma área de ', areabicor, 'm2, teremos ', numerobicos, 'bicos a serem calculados.')
        st.caption('Estas informações são válidas para bicos tipo spray de cobertura padrão, para os demais bicos mude o tipo de bico no menu lateral.')
        alturateto = st.radio(
        'Escolha a faixa de altura do telhado',
        options=['Até 6,1 m','> 6,1 m e <= 9,00 m', '> 9,00 m e <= 18,00 m'])
        if alturateto == 'Até 6,1 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 80','Fator K 115','Fator K 160'])
            if fatork == 'Fator K 80':
                pressaobico = (vazaobico / 80) * (vazaobico / 80)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 80 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)

                st.write('Para o fator K de 80, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada é de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
        elif alturateto == '> 6,1 m e <= 9,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 115','Fator K 160','Fator K 200'])
            if fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 200':
                pressaobico = (vazaobico / 200) * (vazaobico / 200)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 200 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico está vazão ira aumentar.')
        elif alturateto == '> 9,00 m e <= 18,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 115', 'Fator K 160','Fator K 200'])
            if fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
           
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 200':
                pressaobico = (vazaobico / 200) * (vazaobico / 200)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 200 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 950) * 60
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 950 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 60 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')

    #Risco Leve
    if ocupacao == 'asilos e casas de repouso' or ocupacao == 'clubes' or  ocupacao == 'bibliotecas e salas de leituras, exceto salas com prateleiras altas' or ocupacao == 'edifícios residenciais e similares' or ocupacao == 'escolas públicas e privadas (1, 2 e 3 graus)' or ocupacao == 'hospitais com ambulatórios' or ocupacao == 'cirurgia e centros de saúde' or ocupacao == 'hotéis' or ocupacao == 'igrejas' or ocupacao == 'museus' or ocupacao == 'prédios da administração pública' or ocupacao == 'prédios de escritórios, incluindo processamento de dados' or ocupacao == 'áreas de refeição em restaurantes, exceto áreas de serviço' or ocupacao == 'teatros e auditórios exceto palcos e proscênios' :
        st.write('Risco Leve de acordo com a Tabela A.1 da NBR 10.897/20.')
        areaop = st.select_slider(
        'Defina a área de operações:',
        options=['140', '160', '180', '200', '220', '240', '260','280','300','320','340','360','370'])
        if areaop == '140':
            densidade = 6.1
        elif areaop == '160':
            densidade = 5.95
        elif areaop == '180':
            densidade = 5.8
        elif areaop == '200':
            densidade = 5.65
        elif areaop == '220':
            densidade = 5.5
        elif areaop == '240':
            densidade = 5.35
        elif areaop == '260':
            densidade = 5.2
        elif areaop == '280':
            densidade = 5.05
        elif areaop == '300':
            densidade = 4.9
        elif areaop == '320':
            densidade = 4.75
        elif areaop == '340':
            densidade = 4.6
        elif areaop == '360':
            densidade = 4.4
        elif areaop == '370':
            densidade = 4.1
    
        st.write('Para uma área de operação de ', areaop, 'm2, teremos uma densidade de ', densidade, 'lpm/m2')
        tipoteto = st.selectbox('Defina o tipo de teto:',['Não Combustível obstruído','Não obstruído','Combustível não obstruído','Combustível obstruído','Combustíveis com elementos estrutuais distantes < 90 cm'])
        entrebicos = st.number_input('Insira a distância entre bicos no mesmo ramal (m):',value = 1.80)
        if entrebicos > 4.60:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 4.60 m')
        if entrebicos < 1.8:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        entreramais = st.number_input('Insira a distância entre os ramais (m):',value = 1.80)
        if entreramais > 4.60:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser maior que 4.60 m')
        if entreramais < 1.80:
            st.subheader('Por favor entre com outro valor pois esta distância não pode ser menor que 1.80 m')
        areabico = entrebicos * entreramais
        if areabico > 12.1 and tipoteto == 'Combustíveis com elementos estrutuais distantes < 90 cm':
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área para tetos combustíveis com elementos estrutuais distantes < 90 cm não pode ser maior que 12.1 m2')
        if areabico > 15.6 and tipoteto == 'Combustível obstruído':
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área para tetos combustíveis não obstruídos não pode ser maior que 15.6 m2')
        if areabico > 20.9 and tipoteto == 'Não Combustível obstruído':
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área para tetos combustíveis não obstruídos não pode ser maior que 20.9 m2')
        if areabico > 20.9 and tipoteto == 'Não obstruído':
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área para tetos combustíveis não obstruídos não pode ser maior que 20.9 m2')
        if areabico > 20.9 and tipoteto == 'Combustível não obstruído':
            st.subheader('Por favor entre com outras distâncias entre bicos ou ramais pois a área para tetos combustíveis não obstruídos não pode ser maior que 20.9 m2')
        areabicor = round(areabico,2)
        areaopc = int(areaop)    
        numerobico = areaopc / areabico
        vazaobico = densidade * entrebicos * entreramais
        vazaobicor = round(vazaobico,2)
        numerobicos = round(numerobico)
        st.write('A vazão mínima no bico mais desfavorável é de ', vazaobicor ,'lpm.')
        st.write('Considerando que cada bico cobre uma área de ', areabicor, 'm2, teremos ', numerobicos, 'bicos a serem calculados.')
        st.caption('Estas informações são válidas para bicos tipo spray de cobertura padrão, para os demais bicos mude o tipo de bico no menu lateral.')
        alturateto = st.radio(
        'Escolha a faixa de altura do telhado',
        options=['Até 6,1 m','> 6,1 m e <= 9,00 m', '> 9,00 m e <= 18,00 m'])
        if alturateto == 'Até 6,1 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 80','Fator K 115','Fator K 160'])
            if fatork == 'Fator K 80':
                pressaobico = (vazaobico / 80) * (vazaobico / 80)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 80 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)

                st.write('Para o fator K de 80, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 380) * 30
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 380 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 30 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 380) * 30
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 380 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 30 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada é de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 380) * 30
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 380 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 30 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
        elif alturateto == '> 6,1 m e <= 9,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 115','Fator K 160','Fator K 200'])
            if fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 380) * 30
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 380 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 30 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 380) * 30
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 380 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 30 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 200':
                pressaobico = (vazaobico / 200) * (vazaobico / 200)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 200 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico está vazão ira aumentar.')
        elif alturateto == '> 9,00 m e <= 18,00 m':
            fatork = st.radio('Escolha um dos fatores K abaixo', 
            options=['Fator K 115', 'Fator K 160','Fator K 200'])
            if fatork == 'Fator K 115':
                pressaobico = (vazaobico / 115) * (vazaobico / 115)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 115 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 115, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 380) * 30
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 380 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 30 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
           
            if fatork == 'Fator K 160':
                pressaobico = (vazaobico / 160) * (vazaobico / 160)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 160 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 160, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 380) * 30
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 380 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 30 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
            elif fatork == 'Fator K 200':
                pressaobico = (vazaobico / 200) * (vazaobico / 200)
                if pressaobico < 0.5:
                    pressaobico = 0.5
                    vazaobico = 200 * 0.707106781187
                    vazaobicor = round(vazaobico,2)
                pressaobicor = round(pressaobico,2)
                st.write('Para o fator K de 200, será necessário uma pressão de ', pressaobicor, ' bar, para fornecer a vazão calculada de ', vazaobicor,'lpm no bico mais desfavorável.')
                vazaototal = vazaobicor * numerobico
                vazaototalr = round(vazaototal,2)
                st.write('A vazão total do sistema será de no mínimo: ', vazaototalr, 'lpm, porém após o equilíbrio hidráulico esta vazão irá aumentar.')
                st.write('A área máxima de cada VGA deverá ser de 4.800 m2')
                reserva = (vazaototalr + 380) * 30
                reservar = round(reserva,2)
                st.write('A NBR 10.897/20 pede uma vazão adicional de hidrantes de 380 lpm, algumas Instruções Técnicas Estaduais pedem outras vazões.')
                st.write('A reserva deve ser suficiente para suprir o sistema por 30 minutos, portanto a reserva para o sistema de chuveiros automáticos e hidrantes deve ser de no mínimo: ',reservar, 'litros, porém o volume da reserva vai aumentar após o cálculo hidráulico.')
       

elif select == "Spray Est.":
    st.write('Por favor! Aguarde as próximas versões do software.')
    from PIL import Image
    image = Image.open('spkinc1a.png')
    st.image(image)

elif select == "CCAE":
    st.write('Por favor! Aguarde as próximas versões do software.')
    from PIL import Image
    image = Image.open('spkinc1a.png')
    st.image(image)

elif select == "ESFR":
    st.write('Por favor! Aguarde as próximas versões do software.')
    from PIL import Image
    image = Image.open('spkinc1a.png')
    st.image(image)

with st.expander("Responsabilidade Técnica"):
     st.write("""
        Este aplicativo não substitui a responsabilidade do engenheiro pelo projeto, a finalidade é apenas pré dimensionar um sistema para fins de escolha qual a melhor solução de engenharia.
        Para adquirir os conhecimentos necessários para um completo domínio do sistema de chuveiros automáticos e conseguir elaborar o projeto completo visite o site do Professor Silmar Sendin: https://www.silmarsendin.com/cursos-on-line-1
     """)
st.caption('Aplicativo WEB desenvolvido em Python pelo Professor Silmar Sendin.')
