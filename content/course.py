"""Reviewed, aligned study blocks: Danish, English, Brazilian Portuguese.
Originals are indexed in sources/manifest.json. Build requires Python 3 only.
"""
LANGS=('da','en','pt')
def T(da,en,pt): return dict(zip(LANGS,(da,en,pt)))
CHAPTERS=[
T('Logistikmål','Logistics objectives','Objetivos da logística'),
T('Logistisk effektivitet','Logistics efficiency','Eficiência logística'),
T('Virksomhedsbesøg','Company visit','Visita à empresa'),
T('Værdikæden','The value chain','Cadeia de valor'),
T('Supply Chain Management','Supply Chain Management','Gestão da cadeia de suprimentos'),
T('Logistik som konkurrenceparameter','Logistics as a competitive factor','Logística como fator de competição'),
T('Ugeopgaven · NordTrade','Weekly assignment · NordTrade','Trabalho da semana · NordTrade'),
T('Fremlæggelse og evaluering','Presentation and evaluation','Apresentação e avaliação'),
T('IKEA logistikelever','IKEA logistics apprentices','Aprendizes de logística IKEA')]
PAGES=[]
def page(source,title,intro):
 p=dict(source=source,title=title,intro=intro,sections=[]);PAGES.append(p);return p
def S(p,heading,da,en,pt,kind='text'):
 p['sections'].append(dict(heading=heading,body=T(da,en,pt),kind=kind));return p

a=page(0,T('Introduktion og de 7 logistikmål','Introduction and the 7 logistics objectives','Introdução e os 7 objetivos da logística'),T('Følg varen, informationen og kundens behov gennem hele virksomheden.','Follow goods, information and customer needs across the business.','Acompanhe a mercadoria, a informação e a necessidade do cliente por toda a empresa.'))
S(a,T('Hvad er logistik?','What is logistics?','O que é logística?'),
'''Logistik er planlægning og styring af varer, serviceydelser og information fra råvarer til slutkunden. Målet er at opfylde kundens behov og samtidig sikre en rentabel virksomhed.
Det gælder indkøb, varemodtagelse, opbevaring, produktion, pluk, pak, transport og returvarer. En vare kan være fysisk korrekt, men leveringen kan stadig være forkert, hvis tidspunktet, kunden eller informationen er forkert.
IKEA-eksempel: En kunde bestiller en bestemt reol. Varenummer, farve, mål og alle kolli skal passe. Lagerstatus og aftalen om afhentning skal også være korrekte. Eksemplerne her er studieeksempler, som du skal sammenholde med din egen praksis.''',
'''Logistik plans and controls goods, services and information from raw materials to the final customer. It meets customer needs while keeping the business profitable.
It covers indkøb, varemodtagelse, storage, production, pluk, pak, transport and returvarer. A product can be correct while the delivery still fails because the time, customer or information is wrong.
IKEA example: A customer orders a specific bookcase. Its article number, colour, dimensions and all packages must match. Stock information and the collection agreement must also be correct. These are study examples; compare them with your actual workplace.''',
'''Logistik planeja e controla mercadorias, serviços e informações, desde a matéria-prima até o cliente final. Busca atender o cliente e manter a empresa rentável.
Inclui indkøb, varemodtagelse, armazenagem, produção, pluk, pak, transporte e returvarer. O produto pode estar correto e a entrega ainda falhar por causa do horário, destinatário ou informação.
Exemplo IKEA: o cliente pede uma estante específica. Código, cor, medidas e todos os volumes devem corresponder ao pedido. O estoque informado e o acordo de retirada também precisam estar corretos. São exemplos de estudo; compare com a prática real da sua unidade.''')
S(a,T('De syv mål · kontrol før levering','The seven objectives · delivery checklist','Os sete objetivos · conferência da entrega'),
'''Mål | Hvad skal du kontrollere?
Rette produkt | Varenummer, model, farve, mål og variant.
Rette mængde | Antal varer og kolli. Kontrollér både indkøb og salg.
Rette kvalitet | Rigtig standard, ingen skader, komplet og beskyttet emballage.
Rette tid | Aftalt dato og tidspunkt, ikke bare hurtigst muligt.
Rette sted | Rigtigt lager, afdeling, adresse og aflæsningssted.
Rette kunde | Rigtig modtager, ordre, label og dokumentation.
Rette pris | Aftalt pris og fragt samt rimelige samlede logistikomkostninger.
I træningsopgaverne bruges også rette information som det syvende mål. Det erstatter ikke behovet for rigtig kunde: oplysninger om lager, restordrer og levering forbinder alle syv mål. Følg ordlyden i den enkelte opgave.''',
'''Objective | What should you check?
Rette produkt | Article number, model, colour, dimensions and variant.
Rette mængde | Number of items and packages, in purchases and sales.
Rette kvalitet | Required standard, no damage, completeness and protective packaging.
Rette tid | Agreed date and time, rather than simply the fastest delivery.
Rette sted | Correct warehouse, department, address and unloading point.
Rette kunde | Correct recipient, order, label and proof of delivery.
Rette pris | Agreed price and freight, with reasonable total logistics costs.
The exercises also use rette information as the seventh objective. Correct customer identification still matters: stock, backorder and delivery information connects all seven objectives. Follow each assignment’s wording.''',
'''Objetivo | O que conferir?
Rette produkt | Código, modelo, cor, medidas e variante.
Rette mængde | Quantidade de itens e volumes, nas compras e vendas.
Rette kvalitet | Padrão correto, ausência de danos, itens completos e embalagem protetora.
Rette tid | Data e horário combinados, não apenas entregar o mais rápido possível.
Rette sted | Depósito, setor, endereço e local de descarga corretos.
Rette kunde | Destinatário, pedido, etiqueta e comprovante corretos.
Rette pris | Preço e frete acordados, com custos logísticos totais adequados.
Os exercícios também usam rette information como sétimo objetivo. Isso não elimina a identificação correta do cliente: informações de estoque, faltas e entrega conectam os sete objetivos. Siga a formulação de cada tarefa.''')
S(a,T('Hvem har ansvaret?','Who is responsible?','Quem é responsável?'),
'''- Indkøb aftaler produkt, mængde, kvalitet, pris og levering med leverandøren.
- Produktion sikrer kapacitet og det aftalte produkt.
- Lager kontrollerer modtagelse, placering, pluk og pak.
- Salg og kundeservice lover realistiske leveringer og opdaterer kunden.
- Transportøren leverer som aftalt. Virksomheden skal stadig følge op.
3PL udfører eksempelvis transport eller lagerdrift for virksomheden. 4PL koordinerer typisk flere logistiske partnere og den samlede løsning. Tilbageløbslogistik omfatter retur, reparation, genbrug og bortskaffelse.''',
'''- Indkøb agrees products, quantities, quality, price and delivery with suppliers.
- Production provides capacity and the agreed product.
- Lager checks receiving, storage, pluk and pak.
- Sales and customer service make realistic promises and update the customer.
- The carrier delivers as agreed; the business must still follow up.
3PL may carry out transport or warehousing. 4PL typically coordinates several logistics partners and the overall solution. Tilbageløbslogistik covers returns, repairs, reuse and disposal.''',
'''- Indkøb combina produto, quantidade, qualidade, preço e entrega com o fornecedor.
- A produção garante capacidade e produto conforme o acordo.
- Lager confere recebimento, localização, pluk e pak.
- Vendas e atendimento fazem promessas viáveis e atualizam o cliente.
- A transportadora entrega conforme o combinado; a empresa acompanha o resultado.
3PL pode executar transporte ou armazenagem. 4PL normalmente coordena vários parceiros e a solução logística completa. Tilbageløbslogistik inclui devolução, reparo, reutilização e descarte.''')
S(a,T('Kunden, push og pull','The customer, push and pull','O cliente, push e pull'),
'''Ved push sender virksomheden varer frem i kæden ud fra forventet salg. Ved pull udløser kundens efterspørgsel behovet bagud i kæden. I praksis kombineres principperne ofte.
Kortere produktlevetid, kampagner og nye produkter gør efterspørgslen sværere at forudsige. Brug historiske salgstal, lignende produkter, små første indkøb og hyppig opfølgning. En uventet salgsstigning kræver koordinering af indkøb, lager, bemanding og kundeløfter.
Fri fragt er stadig en omkostning for virksomheden. Vurdér ordrestørrelse, avance, returer og transport. Procenttallet om fri fragt i originalen er fra en analyse fra 2019 og er ikke en aktuel markedsmåling.''',
'''With push, goods move forward based on expected sales. With pull, customer demand triggers requirements upstream. Businesses often combine them.
Shorter product lives, campaigns and new products make demand harder to forecast. Use sales history, similar products, small initial orders and frequent reviews. Unexpected growth requires coordination across indkøb, lager, staffing and delivery promises.
Free shipping still costs the business money. Consider order size, margin, returns and transport. The original slide’s free-shipping statistic comes from a 2019 analysis, not a current market survey.''',
'''Em push, a empresa envia produtos adiante com base na previsão de vendas. Em pull, a demanda do cliente aciona as necessidades anteriores da cadeia. Na prática, os dois princípios costumam ser combinados.
Ciclos de produto menores, campanhas e lançamentos dificultam a previsão. Use histórico, produtos semelhantes, pequenos pedidos iniciais e revisão frequente. Um aumento inesperado exige coordenar indkøb, lager, equipe e promessas de entrega.
Frete grátis continua sendo custo da empresa. Avalie tamanho do pedido, margem, devoluções e transporte. O percentual do slide sobre frete grátis vem de uma pesquisa de 2019, não de uma medição atual.''')
S(a,T('Opgaver fra præsentationen','Presentation assignments','Tarefas da apresentação'),
'''1. Lav en planche, som forklarer logistik, og fremlæg den.
2. Vælg et produkt fra din hverdag. Beskriv præcis variant og brug det til at forklare hvert af de syv mål.
3. Undersøg lagerstatus, bestillingsmængder, kvalitetskontrol, emballage, standardleveringstid og modtagelsessted.
4. Hvem har ansvaret for hvert mål i din virksomhed?
5. Diskutér korte produktlevetider, nye produkter og ændringer i salgsmønstre.''',
'''1. Make and present a poster explaining logistik.
2. Choose an everyday product. Specify its exact variant and explain all seven objectives using it.
3. Investigate stock availability, order quantities, quality control, packaging, standard delivery time and receiving point.
4. Who is responsible for each objective in your business?
5. Discuss short product lives, new products and changes in sales patterns.''',
'''1. Faça e apresente um cartaz explicando logistik.
2. Escolha um produto do cotidiano. Especifique a variante exata e use-o para explicar os sete objetivos.
3. Investigue disponibilidade, quantidades de compra, controle de qualidade, embalagem, prazo padrão e local de recebimento.
4. Quem responde por cada objetivo na sua empresa?
5. Discuta ciclos de produto menores, lançamentos e mudanças no padrão de vendas.''','task')
S(a,T('Et eksempel at arbejde videre med','An example to develop','Exemplo para desenvolver'),
'''Vælg en fladpakket reol: Kontrollér artikelnummer og farve (produkt), alle nødvendige kolli (mængde), intakte plader og beslag (kvalitet), bekræftet afhentningstid (tid), aftalt udleveringssted (sted), ordrenummer og identitet efter lokal procedure (kunde), samt korrekt pris og leveringsgebyr (pris). Informér tidligt om mangler. Bekræft de lokale procedurer med din vejleder.''',
'''Choose a flat-packed bookcase: check article number and colour (product), all required packages (quantity), undamaged panels and fittings (quality), confirmed collection time (time), agreed collection point (place), order and identity according to local procedure (customer), and correct price and delivery fee (price). Communicate shortages early. Confirm local procedures with your supervisor.''',
'''Escolha uma estante desmontada: confira código e cor (produto), todos os volumes necessários (quantidade), painéis e ferragens intactos (qualidade), horário confirmado de retirada (tempo), ponto combinado (local), pedido e identidade conforme o procedimento local (cliente), preço e taxa corretos (preço). Avise faltas com antecedência. Confirme os procedimentos locais com a orientadora.''','answer')
a=page(1,T('12 træningshistorier','12 practice scenarios','12 situações para praticar'),T('Find det eller de logistikmål, som ikke er opfyldt. Forklar dit valg med oplysninger fra historien.','Identify the failed logistics objectives. Support your choice with facts from the scenario.','Identifique os objetivos logísticos não atendidos. Justifique com fatos da situação.'))
stories=[
('Runnerskoene','Running shoes','Tênis de corrida','En kunde bestiller løbesko i størrelse 42, men modtager størrelse 40. Tid, pris og stand er korrekte.','A customer orders size 42 running shoes but receives size 40. Time, price and condition are correct.','O cliente pede tênis 42, mas recebe 40. Prazo, preço e estado estão corretos.','Rette produkt: størrelsen er en del af produktets specifikation.','Rette produkt: size is part of the product specification.','Rette produkt: o tamanho faz parte da especificação.'),
('Lageret bugner','An overflowing warehouse','Depósito lotado','En butik bestiller 50 vinterjakker og modtager 120. Der er ikke plads, og mange bliver ikke solgt.','A shop orders 50 winter jackets and receives 120. Storage space is insufficient, and many remain unsold.','Uma loja pede 50 jaquetas de inverno e recebe 120. Falta espaço e muitas não são vendidas.','Rette mængde: 70 jakker for meget.','Rette mængde: 70 excess jackets.','Rette mængde: 70 jaquetas a mais.'),
('Ridset tv','A scratched television','TV arranhada','Et tv har ridser og manglende skruer. Produkt, leveringstid og pris er ellers som aftalt.','A television is scratched and has missing screws. Product, delivery time and price otherwise match the agreement.','Uma TV tem arranhões e faltam parafusos. Produto, prazo e preço correspondem ao combinado.','Rette kvalitet: skader og manglende tilbehør.','Rette kvalitet: damage and missing accessories.','Rette kvalitet: danos e acessórios faltando.'),
('For sent til kamp','Too late for the match','Atraso para o jogo','Fodboldtrøjer til lørdag ankommer mandag. Holdet må bruge de gamle trøjer.','Football shirts needed on Saturday arrive on Monday. The team uses its old shirts.','Camisas para sábado chegam na segunda-feira. O time usa as antigas.','Rette tid: leveringen kommer efter behovet.','Rette tid: delivery occurs after the required time.','Rette tid: a entrega ocorre depois do momento necessário.'),
('Forkert adresse','Wrong address','Endereço errado','Kontorartikler til Aarhus leveres på firmaets adresse i Aalborg.','Office supplies for Aarhus go to the company’s Aalborg address.','Material de escritório destinado a Aarhus chega à unidade de Aalborg.','Rette sted: forkert by og afdeling.','Rette sted: wrong city and branch.','Rette sted: cidade e unidade erradas.'),
('Dyr fragt','Expensive shipping','Frete caro','Den samme telefon koster samlet 500 kr. mere med fragt hos A end hos konkurrenten. Tid og kvalitet er ens.','The same phone costs DKK 500 more including delivery at shop A. Timing and quality are the same.','O mesmo telefone custa DKK 500 a mais com frete na loja A. Prazo e qualidade são iguais.','Rette pris: dårligere samlet pris i sammenligningen. Det er ikke i sig selv bevis for brud på en aftalt pris.','Rette pris: less competitive total price; this alone does not prove a breach of an agreed price.','Rette pris: preço total menos competitivo; isso, por si só, não prova descumprimento de preço acordado.'),
('Ingen besked','No updates','Sem informação','Kunden får kun at vide, at pakken kommer i løbet af ugen. Ingen tracking eller præcis leveringsdag.','The customer is told only that the parcel arrives during the week. No tracking or delivery date is provided.','O cliente só sabe que a encomenda chega durante a semana. Não há rastreamento nem dia definido.','Rette information: kunden mangler anvendelige oplysninger.','Rette information: the customer lacks useful information.','Rette information: faltam informações úteis ao cliente.'),
('T-shirts til firmafesten','Shirts for a company party','Camisetas para a festa','Der bestilles 100 sorte T-shirts med logo. Kun 70 kommer, og 30 af dem er hvide. Levering og pris er korrekte.','100 black logo shirts are ordered. Only 70 arrive; 30 of those are white. Timing and price are correct.','São pedidas 100 camisetas pretas com logo. Chegam 70, das quais 30 são brancas. Prazo e preço estão corretos.','Rette mængde og rette produkt: 30 mangler, og 30 af de leverede har forkert farve.','Rette mængde and rette produkt: 30 are missing and 30 delivered shirts have the wrong colour.','Rette mængde e rette produkt: faltam 30 e outras 30 entregues têm cor errada.'),
('Pizza-kæden','The pizza chain','Rede de pizzarias','Råvarer skal være i centrum kl. 9. Lastbilen kommer kl. 11.30 og kører først til en forkert butik i industrikvarteret.','Ingredients are due downtown at 09:00. The truck arrives at 11:30 and first visits the wrong branch in an industrial district.','Ingredientes deveriam chegar ao centro às 9h. O caminhão chega às 11h30 e primeiro vai à filial errada na área industrial.','Rette tid og rette sted. Der er ikke belæg for at tilføje et tredje mål.','Rette tid and rette sted. The text does not establish a third failure.','Rette tid e rette sted. O texto não comprova um terceiro erro.'),
('Misvisende lagerstatus','Misleading stock status','Estoque informado incorretamente','Webshoppen lover på lager og levering i morgen. Efter bestilling meddeles 10 dages ventetid, fordi musen er udsolgt. Kunden får rabat.','A mouse is advertised in stock for next-day delivery. After ordering, the customer learns of a 10-day wait because it is sold out. A discount is offered.','Um mouse aparece disponível para entrega amanhã. Após a compra, o cliente descobre prazo de dez dias porque acabou. A loja oferece desconto.','Rette information og rette tid. Lager-/mængdeproblemet forklarer fejlen, men teksten oplyser ikke en konkret forkert leveret mængde. Rabat løser ikke forsinkelsen.','Rette information and rette tid. A stock shortage causes the issue, but the text does not specify an incorrect quantity actually delivered. A discount does not fix the delay.','Rette information e rette tid. A falta de estoque causa o problema, mas não há quantidade efetivamente entregue incorreta no texto. O desconto não resolve o atraso.'),
('Juice på tilbud','Promotional juice','Suco em promoção','Juice annonceres til 10 kr. Leverandøren sender en anden variant, halvdelen af mængden, beskadigede og utætte kartoner, en dag for sent og dyrere transport end aftalt.','Juice is advertised at DKK 10. The supplier delivers a different variant, half the quantity, damaged leaking cartons, one day late, with freight above the agreed price.','Suco anunciado a DKK 10: chega outra variante, metade da quantidade, embalagens danificadas e vazando, um dia de atraso e frete acima do combinado.','Rette produkt, mængde, kvalitet, tid og pris.','Rette produkt, mængde, kvalitet, tid and pris.','Rette produkt, mængde, kvalitet, tid e pris.'),
('Medicin til hospitalet','Medicine for a hospital','Medicamento para o hospital','Medicin til operationsafdelingen tirsdag morgen kommer onsdag på forkert afdeling. Der mangler pakker, nogle har forkert styrke, og hospitalet får ingen opdatering.','Medicine due in the operating department on Tuesday morning arrives on Wednesday in the wrong department. Packages are missing, some have the wrong strength, and no updates are provided.','Remédios para o setor cirúrgico na terça de manhã chegam na quarta, em outro setor. Faltam caixas, algumas têm dosagem errada e não há atualizações.','Rette produkt, mængde, tid, sted og information. Forkert styrke er et forkert produkt; diskutér sikkerhed uden at dobbeltoptælle automatisk.','Rette produkt, mængde, tid, sted and information. Incorrect strength is a product error; discuss safety without automatically counting it twice.','Rette produkt, mængde, tid, sted e information. Dosagem errada é erro de produto; discuta segurança sem contar o mesmo erro duas vezes automaticamente.')]
for i,r in enumerate(stories,1):
 S(a,T(f'{i}. {r[0]}',f'{i}. {r[1]}',f'{i}. {r[2]}'),r[3]+'\nHvilke mål er ikke opfyldt?',r[4]+'\nWhich objectives are not met?',r[5]+'\nQuais objetivos não foram atendidos?','task')
 S(a,T(f'{i}. Begrundelse',f'{i}. Explanation',f'{i}. Justificativa'),*r[6:9],kind='answer')

a=page(2,T('Tre cases · vurder alle syv mål','Three cases · assess all seven objectives','Três casos · avalie os sete objetivos'),T('Brug opfyldt, delvist opfyldt eller ikke opfyldt. Vurdér hvert mål særskilt, og foreslå tre forbedringer pr. case.','Use met, partly met or not met. Assess each objective separately and suggest three improvements per case.','Use atendido, parcialmente atendido ou não atendido. Avalie cada objetivo e proponha três melhorias por caso.'))
S(a,T('Case 1 · OfficePartner A/S','Case 1 · OfficePartner A/S','Caso 1 · OfficePartner A/S'),
'''Nordby Kommune bestiller 200 kontorstole, 500 pakker hvidt A4-papir 80 g, 50 kasser gulvrengøring og 20 whiteboards på 120 × 200 cm. Aftalen er levering fredag senest kl. 12 på centrallageret, god stolepris og løbende mail-/portalopdateringer.
Lastbilen kommer fredag kl. 11.30 til det rigtige lager. Der er kun 150 stole. Resten står som restordre på følgesedlen uden forudgående besked. Papiret har rigtig type og antal, men 30 pakker er våde. Rengøringsmidlet har en stærkere koncentration, som kræver en anden blanding. Tre whiteboards har buler. Fakturaen er dyrere end tilbuddet uden forklaring. Kunden får kun beskeden: ordren er sendt.
Vurdér produkt, mængde, kvalitet, tid, sted, pris og information. Find tre forbedringer.''',
'''Nordby municipality orders 200 office chairs, 500 packs of white A4 80 g paper, 50 boxes of floor cleaner and 20 whiteboards measuring 120 × 200 cm. Delivery is promised by Friday noon to the central warehouse, with a favourable chair price and regular email/portal updates.
The truck arrives at the correct warehouse at 11:30 Friday. Only 150 chairs arrive; the backorder appears solely on the delivery note. Paper type and quantity are correct, but 30 packs are wet. The cleaner is more concentrated and needs different dilution. Three boards have dented frames. The invoice exceeds the quotation without explanation. The customer receives only a dispatch notification.
Assess product, quantity, quality, time, place, price and information. Suggest three improvements.''',
'''O município de Nordby pede 200 cadeiras, 500 pacotes de papel A4 branco 80 g, 50 caixas de produto para piso e 20 quadros de 120 × 200 cm. A promessa é entregar até sexta ao meio-dia no depósito central, com preço especial nas cadeiras e atualizações por e-mail/portal.
O caminhão chega ao local correto às 11h30 de sexta. Vêm só 150 cadeiras; as demais constam como pendentes apenas na nota de entrega, sem aviso prévio. Tipo e quantidade de papel estão corretos, mas 30 pacotes molharam. O produto de limpeza é mais concentrado e exige outra diluição. Três quadros têm a moldura amassada. A fatura supera a proposta, sem explicação. O único aviso recebido informa que o pedido saiu.
Avalie produto, quantidade, qualidade, prazo, local, preço e informação. Proponha três melhorias.''','task')
S(a,T('OfficePartner · vurdering','OfficePartner · assessment','OfficePartner · avaliação'),
'''Mål | Vurdering og begrundelse
Rette produkt | Delvist: korrekt papir og whiteboards, men ændret rengøringsvariant er ikke bekræftet som accepteret.
Rette mængde | Ikke opfyldt: 50 stole mangler.
Rette kvalitet | Delvist: 30 papirpakker og 3 whiteboards er skadet.
Rette tid | Delvist: lastbilen er rettidig, men hele ordren er ikke leveret inden fristen.
Rette sted | Opfyldt: centrallageret i Nordby.
Rette pris | Ikke opfyldt: faktura stemmer ikke med tilbuddet.
Rette information | Ikke opfyldt: ingen tidlig besked om restordre eller ændringer.
Tre forbedringer: reservér varer før bekræftelse; indfør kvalitets- og emballagekontrol; synkronisér tilbud, faktura og kundeinformation. En ankomst til tiden er ikke det samme som en komplet rettidig ordre.''',
'''Objective | Assessment and evidence
Rette produkt | Partly: paper and boards match, but acceptance of the changed cleaner variant is unconfirmed.
Rette mængde | Not met: 50 chairs are missing.
Rette kvalitet | Partly: 30 paper packs and 3 boards are damaged.
Rette tid | Partly: truck arrives on time but the full order misses the deadline.
Rette sted | Met: Nordby central warehouse.
Rette pris | Not met: invoice differs from quotation.
Rette information | Not met: no early backorder or change notice.
Three improvements: reserve stock before confirmation; check quality and packaging; synchronise quotations, invoices and customer updates. An on-time truck is not necessarily a complete on-time order.''',
'''Objetivo | Avaliação e evidência
Rette produkt | Parcial: papel e quadros corretos; não há confirmação de aceite da variante do produto de limpeza.
Rette mængde | Não atendido: faltam 50 cadeiras.
Rette kvalitet | Parcial: 30 pacotes de papel e 3 quadros danificados.
Rette tid | Parcial: caminhão pontual, mas pedido completo fora do prazo.
Rette sted | Atendido: depósito central de Nordby.
Rette pris | Não atendido: fatura diferente da proposta.
Rette information | Não atendido: falta aviso antecipado sobre pendências e mudanças.
Três melhorias: reservar estoque antes de confirmar; conferir qualidade e proteção da carga; sincronizar proposta, fatura e avisos ao cliente. Caminhão pontual não significa pedido completo pontual.''','answer')
S(a,T('Case 2 · AgroTek A/S','Case 2 · AgroTek A/S','Caso 2 · AgroTek A/S'),
'''Møllebjerg Landbrug bestiller en bestemt mejetærsker klar til brug senest 1. august, sliddele til ny og gammel maskine samt årligt eftersyn og hurtig hjælp ved driftsstop. AgroTek lover levering på gårdspladsen, instruktør, alle sliddele på lager, kampagnepris til 30. juni og opdateret portal.
Maskinen kommer 2. august. Kunden får først besked aftenen før, da han selv ringer. Modellen og maskinens stand er korrekte, men nogle dele kommer først en uge senere. Instruktøren er syg. Manual og video erstatter besøget, men internetforbindelsen på gården er dårlig. Maskinprisen er korrekt; et ikke-aftalt gebyr for hurtig levering tilføjes. Maskinen står rigtigt, mens en reservedelspalle står ved forkert lade. Portalen viser fejlagtigt alle dele på lager. Serviceaftalens PDF mangler klare responstider og betingelser.
Vurdér de syv mål, og foreslå tre forbedringer.''',
'''Møllebjerg farm orders a specified combine harvester ready by 1 August, wear parts for its new and old machines, annual servicing and rapid breakdown support. AgroTek promises farmyard delivery, an instructor, all wear parts in stock, a campaign price valid until 30 June and an updated portal.
The machine arrives on 2 August. The farmer learns this only the previous evening after calling. Model and condition are correct, but some parts arrive a week later. The instructor is sick; an online manual/video is unsuitable because the farm connection is poor. The agreed machine price is honoured, but an unagreed express fee is added. The machine is correctly placed; a parts pallet goes to the wrong barn. The portal falsely shows all parts available. The service PDF lacks clear response times and conditions.
Assess all seven objectives and suggest three improvements.''',
'''A fazenda Møllebjerg pede uma colheitadeira específica pronta até 1º de agosto, peças de desgaste para a máquina nova e a antiga, revisão anual e atendimento rápido em paradas. AgroTek promete entrega no pátio, instrutor, todas as peças em estoque, preço promocional válido até 30 de junho e portal atualizado.
A máquina chega em 2 de agosto. O agricultor só descobre na véspera, ao telefonar. Modelo e estado estão corretos, mas algumas peças chegam uma semana depois. O instrutor adoece; manual e vídeo online não atendem bem porque a conexão da fazenda é ruim. O preço da máquina é respeitado, mas aparece taxa de urgência não acordada. A máquina está no pátio correto; uma palete de peças vai ao galpão errado. O portal informa falsamente todas as peças disponíveis. O PDF do contrato não esclarece prazos e condições de atendimento.
Avalie os sete objetivos e proponha três melhorias.''','task')
S(a,T('AgroTek · vurdering','AgroTek · assessment','AgroTek · avaliação'),
'''Mål | Vurdering og begrundelse
Rette produkt | Opfyldt for maskinen: rigtig model. Manglende dele vurderes under mængde.
Rette mængde | Ikke opfyldt: dele mangler.
Rette kvalitet | Delvist: maskinen er fejlfri, men lovet instruktion og serviceindhold er utilstrækkeligt leveret.
Rette tid | Ikke opfyldt: 2. august frem for 1. august; nogle dele yderligere forsinket.
Rette sted | Delvist: maskinen er korrekt placeret, reservedelspallen ikke.
Rette pris | Delvist: rigtig maskinpris, men ikke-aftalt gebyr.
Rette information | Ikke opfyldt: forkert lagerstatus, sen besked og uklare servicevilkår.
Tre forbedringer: opdatér lager/portal i realtid; planlæg reserveinstruktør og offline vejledning; bekræft leveringssted, gebyrer og serviceresponstid skriftligt. En anden vurdering kan forsvares, hvis du tydeligt adskiller maskinens kvalitet fra serviceydelsens.''',
'''Objective | Assessment and evidence
Rette produkt | Met for the machine: correct model. Missing parts belong under quantity.
Rette mængde | Not met: missing parts.
Rette kvalitet | Partly: machine is sound, but promised instruction and service are inadequately delivered.
Rette tid | Not met: 2 August instead of 1 August, with later parts.
Rette sted | Partly: machine correct, parts pallet wrong.
Rette pris | Partly: correct machine price, unagreed fee.
Rette information | Not met: false stock data, late notice and unclear service terms.
Three improvements: live stock/portal updates; backup instructor and offline guidance; written confirmation of location, fees and service response. Alternative ratings are defensible if product and service quality are clearly distinguished.''',
'''Objetivo | Avaliação e evidência
Rette produkt | Atendido para a máquina: modelo correto. Peças ausentes entram em quantidade.
Rette mængde | Não atendido: faltam peças.
Rette kvalitet | Parcial: máquina sem defeito; instrução e serviço prometidos insuficientes.
Rette tid | Não atendido: 2 em vez de 1º de agosto; peças ainda mais atrasadas.
Rette sted | Parcial: máquina no local correto, palete no galpão errado.
Rette pris | Parcial: preço da máquina correto, taxa não combinada.
Rette information | Não atendido: estoque falso, aviso tardio e contrato pouco claro.
Três melhorias: atualizar portal/estoque; prever instrutor substituto e orientação offline; confirmar local, taxas e prazo de atendimento por escrito. Outras avaliações podem ser defendidas se distinguirem claramente a qualidade do produto e do serviço.''','answer')
S(a,T('Case 3 · HomeBox','Case 3 · HomeBox','Caso 3 · HomeBox'),
'''Sommerkampagne i Storby-Centret: 500 altansæt, 300 loungesæt, 1.000 puder og 200 parasoller med betonfod. Varerne skal være klar to uger før kampagnen. Reklamernes modeller og priser skal passe, og lagerstatus skal være opdateret.
Containerne når centrallageret kun en uge før kampagnen. Direkte videresendelse blander modeller og farver. Butikken får 350 altansæt, heraf 100 i forkert reklamefarve; 200 loungesæt; 1.000 puder, heraf 150 med fejl; og 150 parasoller. Levering sker om aftenen tre dage før start, så personalet arbejder om natten.
Nogle reklamevarer findes kun i lignende udgaver. Loungesæt bliver udsolgt ved middagstid uden reserve på centrallageret. Kassepriser er nogle steder højere end tilbudsavisen. Systemet viser 25 parasoller, selvom de næsten er solgt. Chefen får kun uklare meldinger om forsinkelser.
Vurdér alle syv mål, og foreslå tre forbedringer.''',
'''Storby-Centret summer campaign: 500 balcony sets, 300 lounge sets, 1,000 cushions and 200 parasols with concrete bases. Goods must be ready two weeks before launch. Advertised models/prices and stock data must match.
Containers reach the central warehouse only a week before launch. Direct forwarding mixes models/colours. The shop receives 350 balcony sets, including 100 in an unadvertised colour; 200 lounge sets; 1,000 cushions, including 150 faulty ones; and 150 parasols. Delivery occurs three evenings before launch, requiring night work.
Some advertised items are replaced by similar variants. Lounge sets sell out by noon without central reserve. Some checkout prices exceed the leaflet. The system still shows 25 parasols although nearly sold. The manager receives vague delay updates.
Assess all seven objectives and suggest three improvements.''',
'''Campanha de verão em Storby-Centret: 500 conjuntos de varanda, 300 de lounge, 1.000 almofadas e 200 guarda-sóis com base de concreto. Tudo deveria estar pronto duas semanas antes. Modelos/preços da publicidade e estoque informado precisam corresponder.
Os contêineres chegam ao depósito central só uma semana antes. O envio direto mistura modelos e cores. A loja recebe 350 conjuntos de varanda, sendo 100 em cor diferente do anúncio; 200 de lounge; 1.000 almofadas, das quais 150 com defeito; e 150 guarda-sóis. A entrega acontece à noite, três dias antes do início, exigindo trabalho noturno.
Alguns itens anunciados só existem em versões semelhantes. Os conjuntos de lounge acabam ao meio-dia, sem reserva central. Alguns preços no caixa superam o encarte. O sistema indica 25 guarda-sóis, embora quase todos já estejam vendidos. A gerente recebe apenas avisos vagos de atraso.
Avalie os sete objetivos e proponha três melhorias.''','task')
S(a,T('HomeBox · vurdering','HomeBox · assessment','HomeBox · avaliação'),
'''Mål | Vurdering og begrundelse
Rette produkt | Delvist: 100 altansæt har anden farve; ikke alle reklameprodukter findes.
Rette mængde | Ikke opfyldt: mangler 150 altansæt, 100 loungesæt og 50 parasoller.
Rette kvalitet | Delvist: 150 puder er fejlbehæftede, 850 er ikke beskrevet som defekte.
Rette tid | Ikke opfyldt: tre dage før start i stedet for to uger.
Rette sted | Opfyldt for den beskrevne butikslevering. Forkerte modeller i andre butikker beviser ikke forkert adresse her.
Rette pris | Ikke opfyldt: kassen viser højere priser end annonceret.
Rette information | Ikke opfyldt: forkert lagerstatus og uklare leveringsbeskeder.
Tre forbedringer: fælles kampagneplan med lagerreservation og tidsbuffer; scanning af model, farve og antal; synkroniserede priser, lagerstatus og afvigelsesalarmer. Begrund vurderingen: tabellen er et løsningsforslag, ikke en eneste tilladt formulering.''',
'''Objective | Assessment and evidence
Rette produkt | Partly: 100 balcony sets have a different colour and advertised items are missing.
Rette mængde | Not met: short by 150 balcony sets, 100 lounge sets and 50 parasols.
Rette kvalitet | Partly: 150 faulty cushions; 850 are not described as faulty.
Rette tid | Not met: three days before launch rather than two weeks.
Rette sted | Met for the described shop delivery. Mixed models at other branches do not establish a wrong address here.
Rette pris | Not met: checkout prices exceed advertised prices.
Rette information | Not met: wrong stock data and vague delivery updates.
Three improvements: shared campaign plan with reservations and buffer; scan model, colour and quantity; synchronise prices/stock and flag exceptions. This is a reasoned example, not the only defensible wording.''',
'''Objetivo | Avaliação e evidência
Rette produkt | Parcial: 100 conjuntos têm outra cor; faltam produtos anunciados.
Rette mængde | Não atendido: faltam 150 conjuntos de varanda, 100 de lounge e 50 guarda-sóis.
Rette kvalitet | Parcial: 150 almofadas defeituosas; as outras 850 não são descritas como defeituosas.
Rette tid | Não atendido: três dias antes em vez de duas semanas.
Rette sted | Atendido na entrega à loja descrita. Modelos trocados em outras filiais não comprovam endereço errado aqui.
Rette pris | Não atendido: preço no caixa superior ao anúncio.
Rette information | Não atendido: estoque incorreto e avisos vagos.
Três melhorias: planejar campanha em conjunto, reservando estoque e folga de prazo; escanear modelo, cor e quantidade; sincronizar preços/estoque e alertar desvios. É uma resposta fundamentada, não a única formulação aceitável.''','answer')
a=page(3,T('Service, omkostninger og beregninger','Service, costs and calculations','Serviço, custos e cálculos'),T('Logistisk effektivitet er balancen mellem leveringsservice og de samlede logistikomkostninger.','Logistics efficiency balances delivery service against total logistics costs.','Eficiência logística equilibra o serviço de entrega e os custos logísticos totais.'))
S(a,T('Fem serviceområder og fem omkostningsområder','Five service areas and five cost areas','Cinco dimensões de serviço e cinco de custo'),
'''Leveringsservice | Logistikomkostninger
Leveringstid | Lageromkostninger
Lagerservicegrad | Transportomkostninger
Leveringsoverholdelse | Emballage- og håndteringsomkostninger
Leveringsfleksibilitet | Administrative omkostninger
Leveringsinformation | Mangelomkostninger
Kolonnerne er to lister, ikke parvise årsagssammenhænge. Trade-off: højere lager kan forbedre tilgængelighed, men øger kapitalbinding. Trade-up: en bedre proces kan både forkorte leveringstid og reducere lagerbehov.
Leveringsfleksibilitet omfatter nye produkter, produktvarianter, mængder og leveringssteder. Leveringsinformation handler om rettidige oplysninger om blandt andet ændret dato og antal. Scanning, ERP, WMS, GPS og track & trace virker kun, når data opdateres korrekt.''',
'''Delivery service (Leveringsservice) | Logistics costs (Logistikomkostninger)
Delivery time (Leveringstid) | Warehouse costs (Lageromkostninger)
Immediate stock service (Lagerservicegrad) | Transport costs (Transportomkostninger)
On-time delivery (Leveringsoverholdelse) | Packaging and handling costs (Emballage- og håndteringsomkostninger)
Delivery flexibility (Leveringsfleksibilitet) | Administration costs (Administrative omkostninger)
Delivery information (Leveringsinformation) | Shortage costs (Mangelomkostninger)
These are two lists, not row-by-row causal pairs. Trade-off: more inventory can improve availability but increases lagerbinding. Trade-up: a better process can shorten delivery time and reduce stock needs together.
Leveringsfleksibilitet includes new products, variants, quantities and delivery locations. Leveringsinformation means timely updates about changes such as date and quantity. Scanning, ERP, WMS, GPS and tracking depend on accurate updates.''',
'''Serviço de entrega (Leveringsservice) | Custos logísticos (Logistikomkostninger)
Prazo de entrega (Leveringstid) | Custos de armazenagem (Lageromkostninger)
Nível de atendimento imediato pelo estoque (Lagerservicegrad) | Custos de transporte (Transportomkostninger)
Cumprimento do prazo (Leveringsoverholdelse) | Custos de embalagem e manuseio (Emballage- og håndteringsomkostninger)
Flexibilidade de entrega (Leveringsfleksibilitet) | Custos administrativos (Administrative omkostninger)
Informações de entrega (Leveringsinformation) | Custos da falta de produtos (Mangelomkostninger)
São duas listas, não relações de causa por linha. Trade-off: mais estoque pode melhorar a disponibilidade, mas aumenta lagerbinding. Trade-up: melhorar um processo pode reduzir prazo e necessidade de estoque ao mesmo tempo.
Leveringsfleksibilitet envolve novos produtos, variantes, quantidades e locais de entrega. Leveringsinformation é informar mudanças de data e quantidade em tempo hábil. Scanning, ERP, WMS, GPS e rastreamento dependem de registros corretos.''')
S(a,T('Formler · vælg den rigtige måleenhed','Formulas · choose the right unit','Fórmulas · escolha a unidade correta'),
'''Nøgletal | Beregning
Lead time | Teknisk behandling + ordrebehandling + indkøb + produktion + distribution, når trinene følger efter hinanden.
GAB | Virksomhedens lead time minus kundens accepterede leveringstid.
Lagerservicegrad, ordrer | Komplette ordrer leveret fra lager / bestilte ordrer × 100.
Lagerservicegrad, enheder | Enheder leveret fra lager / bestilte enheder × 100.
Leveringsoverholdelse, enheder | Rettidigt leverede enheder / relevante leverede enheder × 100.
Omsætningshastighed | Årets vareforbrug til kostpris / gennemsnitlig lagerværdi til kostpris.
Gennemsnitlige lagerdage | 365 / årets omsætningshastighed, hvis en 365-dages konvention anvendes.
Logistikomkostning i procent | Samlede logistikomkostninger / omsætning × 100.
Bland ikke enheder, ordrelinjer og hele ordrer. Nævn altid nævneren. Originalens formulering om komplette ordrer måler komplethed; rettidighed kræver også en aftalt dato. Lageromsætning bruger vareforbrug, ikke salgsomsætning.''',
'''Measure | Calculation
Lead time | Technical processing + order processing + purchasing + production + distribution, when stages are sequential.
GAB | Business lead time minus the customer’s acceptable delivery time.
Immediate stock service (Lagerservicegrad), orders | Complete orders fulfilled from stock / orders placed × 100.
Immediate stock service (Lagerservicegrad), units | Units fulfilled from stock / units ordered × 100.
On-time delivery (Leveringsoverholdelse), units | Units delivered on time / relevant delivered units × 100.
Inventory turnover (Omsætningshastighed) | Annual cost of goods consumed / average stock at cost.
Average Inventory days (lagerdage) | 365 / annual stock turnover, under a 365-day convention.
Logistics costs (Logistikomkostninger) percentage | Total logistics costs / revenue × 100.
Do not mix units, order lines and complete orders. State the denominator. The original’s complete-order formula measures completeness; punctuality also requires an agreed date. Stock turnover uses consumption at cost, not sales revenue.''',
'''Indicador | Cálculo
Lead time | Processamento técnico + pedido + compras + produção + distribuição, quando as etapas são sequenciais.
GAB | Lead time da empresa menos o prazo aceito pelo cliente.
Nível de atendimento imediato pelo estoque (Lagerservicegrad), pedidos | Pedidos completos atendidos do estoque / pedidos recebidos × 100.
Nível de atendimento imediato pelo estoque (Lagerservicegrad), unidades | Unidades atendidas do estoque / unidades pedidas × 100.
Cumprimento do prazo (Leveringsoverholdelse), unidades | Unidades entregues no prazo / unidades entregues pertinentes × 100.
Giro de estoque (Omsætningshastighed) | Consumo anual de mercadorias a custo / estoque médio a custo.
Dias de estoque (Lagerdage) médios | 365 / giro anual, usando a convenção de 365 dias.
Percentual de Custos logísticos (logistikomkostninger) | Custos logísticos totais / faturamento × 100.
Não misture unidades, linhas e pedidos completos. Declare o denominador. A fórmula de pedidos completos do original mede completude; pontualidade também exige a data acordada. O giro usa consumo a custo, não faturamento.''')
S(a,T('Forstå omkostningerne','Understand the costs','Entenda os custos'),
'''- Lageromkostninger: husleje, løn, trucks, reoler, svind og forrentning af kapital i lager.
- Transportomkostninger: interne flytninger og ekstern transport. For 3PL bruges aftale og faktura. For egen transport medregnes bil, løn, brændstof, vedligehold og kapacitet.
- Emballage: materiale, arbejdstid, maskiner, design, håndtering og affald. Lønomkostning pr. kasse = timeløn / kasser pr. time.
- Administration: løn og IT til ordrer og koordinering. Mange små ordrer, dobbeltindtastning og særprocedurer øger tidsforbruget. EDI og standardiserede processer kan hjælpe.
- Mangelomkostninger: tabt dækningsbidrag, hastefragt, nødkøb og andre følger af manglende levering. Undgå at tælle den samme mistede indtjening to gange.
En lav indkøbspris kan give højere totalomkostning gennem lager, fejl og transport.''',
'''- Warehouse costs (Lageromkostninger): rent, staff, trucks, racks, shrinkage and capital costs.
- Transport costs (Transportomkostninger): internal moves and external freight. Use the 3PL agreement/invoice; own transport also includes vehicles, wages, fuel, maintenance and capacity.
- Packaging: materials, labour, machines, design, handling and waste. Labour per box = hourly wage / boxes packed per hour.
- Administration: labour and IT for orders and coordination. Small orders, duplicate entry and exceptions take time. EDI and standard processes can help.
- Shortage costs (Mangelomkostninger): lost dækningsbidrag, emergency freight/purchases and other shortage consequences. Do not double-count lost earnings.
A cheap purchase price may increase total costs through storage, errors and transport.''',
'''- Custos de armazenagem (Lageromkostninger): aluguel, equipe, empilhadeiras, estruturas, perdas e custo do capital em estoque.
- Custos de transporte (Transportomkostninger): movimentações internas e frete externo. Para 3PL, use contrato/fatura; transporte próprio também inclui veículo, salários, combustível, manutenção e capacidade.
- Embalagem: material, trabalho, máquinas, projeto, manuseio e descarte. Mão de obra por caixa = salário por hora / caixas embaladas por hora.
- Administração: salários e TI para pedidos e coordenação. Pedidos pequenos, digitação duplicada e exceções consomem tempo. EDI e processos padronizados ajudam.
- Custos da falta de produtos (Mangelomkostninger): dækningsbidrag perdido, frete urgente, compras emergenciais e outros efeitos da falta. Não conte a mesma receita perdida duas vezes.
Preço de compra baixo pode elevar o custo total por estoque, erros e transporte.''')
S(a,T('Tre regneopgaver','Three calculation exercises','Três exercícios de cálculo'),
'''1. Lead time: teknisk behandling 1 dag, ordrebehandling 1, indkøb 5, produktion 3 og distribution 2. Kunden accepterer 7 dage. Beregn samlet tid og GAB.
2. Pakning: kasse 4,00 kr., fyld 1,50 kr., tape/label 0,50 kr. Timeløn 200 kr.; 40 kasser i timen. Find materialer, løn, total pr. kasse og total for 350 kasser.
3. SneakX: 80 par bestilt, 50 på lager og 10 ekstra skaffes til en merpris på 100 kr. pr. par. Dækningsbidrag er normalt 150 kr. pr. par. Find tabte salg, tabt dækningsbidrag, meromkostning og omkostningstype.''',
'''1. Lead time: technical work 1 day, order processing 1, purchasing 5, production 3 and distribution 2. Customer accepts 7 days. Find total time and GAB.
2. Packing: box DKK 4.00, filler 1.50, tape/label 0.50. Wage DKK 200/hour; 40 boxes/hour. Find materials, labour, cost per box and cost for 350 boxes.
3. SneakX: 80 pairs ordered, 50 stocked and 10 emergency pairs bought at DKK 100 extra each. Normal dækningsbidrag is DKK 150/pair. Find lost sales, lost contribution, extra cost and cost category.''',
'''1. Lead time: trabalho técnico 1 dia, pedido 1, compras 5, produção 3 e distribuição 2. O cliente aceita 7 dias. Calcule tempo total e GAB.
2. Embalagem: caixa DKK 4,00; enchimento 1,50; fita/etiqueta 0,50. Salário DKK 200/hora; 40 caixas/hora. Ache material, mão de obra, total por caixa e por 350 caixas.
3. SneakX: 80 pares pedidos, 50 em estoque e 10 comprados emergencialmente por DKK 100 adicionais/par. Dækningsbidrag normal DKK 150/par. Ache vendas perdidas, contribuição perdida, custo adicional e categoria do custo.''','task')
S(a,T('Beregninger trin for trin','Calculations step by step','Cálculos passo a passo'),
'''1. Lead time = 1 + 1 + 5 + 3 + 2 = 12 dage. GAB = 12 − 7 = 5 dage. Ja, der er et gab. Kortere processer eller lagerføring kan undersøges.
2. Materialer = 4 + 1,50 + 0,50 = 6 kr. Løn = 200 / 40 = 5 kr. Total = 11 kr. pr. kasse. 350 × 11 = 3.850 kr. Opgaven opgiver ingen maskinomkostning; tilføj ikke den ekstra krone fra et andet eksempel på en anden slide.
3. Leveret = 50 + 10 = 60 par. Tabte salg = 80 − 60 = 20 par. Tabt dækningsbidrag = 20 × 150 = 3.000 kr. Nødkøbets meromkostning = 10 × 100 = 1.000 kr. Samlet mangelomkostning i dette forenklede eksempel = 4.000 kr.''',
'''1. Lead time = 1 + 1 + 5 + 3 + 2 = 12 days. GAB = 12 − 7 = 5 days. A gap exists. Investigate process reductions or stocking.
2. Materials = 4 + 1.50 + 0.50 = DKK 6. Labour = 200 / 40 = DKK 5. Total = DKK 11/box. 350 × 11 = DKK 3,850. No machine cost is given; do not import the extra DKK 1 from the separate worked example.
3. Delivered = 50 + 10 = 60 pairs. Lost sales = 80 − 60 = 20. Lost dækningsbidrag = 20 × 150 = DKK 3,000. Emergency premium = 10 × 100 = DKK 1,000. Combined shortage cost in this simplified example = DKK 4,000.''',
'''1. Lead time = 1 + 1 + 5 + 3 + 2 = 12 dias. GAB = 12 − 7 = 5 dias. Existe diferença. Investigue redução de processos ou manutenção de estoque.
2. Material = 4 + 1,50 + 0,50 = DKK 6. Mão de obra = 200 / 40 = DKK 5. Total = DKK 11/caixa. 350 × 11 = DKK 3.850. Não foi dado custo de máquina; não acrescente a coroa de outro exemplo dos slides.
3. Entregues = 50 + 10 = 60 pares. Vendas perdidas = 80 − 60 = 20. Dækningsbidrag perdido = 20 × 150 = DKK 3.000. Adicional emergencial = 10 × 100 = DKK 1.000. Custo total da falta, neste exemplo simplificado = DKK 4.000.''','answer')

a=page(4,T('Bogens opgaver 2.1–2.7','Textbook exercises 2.1–2.7','Exercícios do livro 2.1–2.7'),T('Historiske undervisningscases fra de syv scannede sider. Tal beskriver casene, ikke virksomhedernes situation i dag.','Historical teaching cases from seven scanned pages. Figures describe the cases, not the companies today.','Casos didáticos históricos das sete páginas digitalizadas. Os números descrevem os casos, não as empresas atualmente.'))
S(a,T('2.1 · Kabin A/S','2.1 · Kabin A/S','2.1 · Kabin A/S'),
'''Kabin designer og fremstiller kabinetter til elektronik på tre danske fabrikker. Omsætning: 700 mio. kr.; aktiver: 710 mio. kr.; eksport: 80 % gennem otte egne salgsselskaber. USA aftager ca. 35 % af omsætningen. Lead time er 5 uger mod kundekrav på 2 uger. Leveringsoverholdelse er 60 %. Det amerikanske salgsselskab opbygger ekstra sikkerhedslager uden at orientere fabrikkernes planlæggere, efter at terminer er flyttet 3–4 gange.
Ordre | Bestilt | Leveret | Aftalt uge | Leveret uge
12222 | 50 | 20 | 1 | 2
33221 | 60 | 60 | 2 | 3
33322 | 20 | 15 | 2 | 4
55331 | 100 | 100 | 3 | 5
44111 | 150 | 110 | 3 | 5
12223 | 30 | 15 | 3 | 6
22311 | 45 | 40 | 7 | 7
77666 | 55 | 25 | 7 | 8
99777 | 50 | 50 | 8 | 8
76555 | 70 | 40 | 8 | 9
55544 | 234 | 180 | 8 | 9
76544 | 75 | 60 | 9 | 9
88666 | 40 | 40 | 9 | 12
44211 | 80 | 80 | 9 | 17
77555 | 75 | 60 | 9 | 9
1. Beskriv leveringsservicen. 2. Vurdér lagerservicegraden. 3. Forklar konsekvensen af USA’s strategi.''',
'''Kabin designs and manufactures electronic enclosures at three Danish factories. Revenue: DKK 700m; assets: 710m; exports: 80% through eight owned sales companies. USA accounts for about 35% of revenue. Lead time is 5 weeks versus a 2-week customer requirement. Leveringsoverholdelse is 60%. After dates are moved 3–4 times, the US subsidiary builds hidden sikkerhedslager without informing factory planners.
Order | Ordered | Delivered | Promised week | Actual week
12222 | 50 | 20 | 1 | 2
33221 | 60 | 60 | 2 | 3
33322 | 20 | 15 | 2 | 4
55331 | 100 | 100 | 3 | 5
44111 | 150 | 110 | 3 | 5
12223 | 30 | 15 | 3 | 6
22311 | 45 | 40 | 7 | 7
77666 | 55 | 25 | 7 | 8
99777 | 50 | 50 | 8 | 8
76555 | 70 | 40 | 8 | 9
55544 | 234 | 180 | 8 | 9
76544 | 75 | 60 | 9 | 9
88666 | 40 | 40 | 9 | 12
44211 | 80 | 80 | 9 | 17
77555 | 75 | 60 | 9 | 9
1. Describe delivery service. 2. Assess lagerservicegrad. 3. Explain the consequences of the US strategy.''',
'''Kabin projeta e fabrica gabinetes eletrônicos em três fábricas dinamarquesas. Faturamento: DKK 700 milhões; ativos: 710 milhões; exportação: 80% por oito subsidiárias próprias. Os EUA representam aproximadamente 35% das vendas. Lead time de 5 semanas para exigência de 2 semanas. Leveringsoverholdelse de 60%. Após 3–4 adiamentos, a subsidiária americana monta sikkerhedslager sem informar os planejadores.
Pedido | Pedido em unidades | Entregue | Semana acordada | Semana real
12222 | 50 | 20 | 1 | 2
33221 | 60 | 60 | 2 | 3
33322 | 20 | 15 | 2 | 4
55331 | 100 | 100 | 3 | 5
44111 | 150 | 110 | 3 | 5
12223 | 30 | 15 | 3 | 6
22311 | 45 | 40 | 7 | 7
77666 | 55 | 25 | 7 | 8
99777 | 50 | 50 | 8 | 8
76555 | 70 | 40 | 8 | 9
55544 | 234 | 180 | 8 | 9
76544 | 75 | 60 | 9 | 9
88666 | 40 | 40 | 9 | 12
44211 | 80 | 80 | 9 | 17
77555 | 75 | 60 | 9 | 9
1. Descreva o serviço. 2. Avalie lagerservicegrad. 3. Explique as consequências da estratégia americana.''','task')
S(a,T('2.1 · beregning og fortolkning','2.1 · calculation and interpretation','2.1 · cálculo e interpretação'),
'''Leveringsservice er utilstrækkelig: gab på 3 uger og kun 60 % leveringsoverholdelse ifølge casebeskrivelsen.
Januar: 410 bestilt, 320 leveret → 78,05 % på enhedsbasis. 2 af 6 ordrer er komplette → 33,33 %.
Februar: 724 bestilt, 575 leveret → 79,42 %. 3 af 9 er komplette → 33,33 %.
Samlet: 895 / 1.134 × 100 = 78,92 % i leveret mængde. Komplette ordrer: 5 / 15 = 33,33 %.
Vigtigt: tabellerne viser realiserede leveringer og datoer, ikke eksplicit levering direkte fra lager. Disse procenter er derfor en vurdering af opfyldelsesgrad som proxy; en præcis lagerservicegrad kræver viden om, hvad der blev leveret straks fra lager. Rettidig og komplet er en anden måling: kun ordre 99777 opfylder begge i stikprøven. Bland ikke stikprøven med virksomhedens oplyste 60 %.
USA’s skjulte lager giver mere kapitalbinding, risiko for ukurans og falske efterspørgselssignaler. Del faktiske salg og lagerdata og lav én fælles plan frem for at bestille ekstra i skjul.''',
'''Service is inadequate: a 3-week gap and only 60% leveringsoverholdelse in the narrative.
January: 410 ordered, 320 delivered → 78.05% by units. 2/6 complete orders → 33.33%.
February: 724 ordered, 575 delivered → 79.42%. 3/9 complete → 33.33%.
Combined: 895 / 1,134 × 100 = 78.92% by delivered quantity; 5/15 complete orders = 33.33%.
The tables show realised deliveries/dates, not explicitly immediate stock fulfilment. These are fulfilment proxies; precise lagerservicegrad requires immediate-from-stock data. On-time-and-complete is another measure: only order 99777 meets both in this sample. Do not confuse the sample with the stated company-wide 60%.
Hidden US inventory increases capital tied up, obsolescence and distorted demand signals. Share actual sales/stock and make one coordinated plan.''',
'''O serviço é insuficiente: diferença de 3 semanas e apenas 60% de leveringsoverholdelse na descrição.
Janeiro: 410 unidades pedidas, 320 entregues → 78,05%. Pedidos completos: 2/6 = 33,33%.
Fevereiro: 724 pedidas, 575 entregues → 79,42%. Completos: 3/9 = 33,33%.
Total: 895 / 1.134 × 100 = 78,92% da quantidade; 5/15 pedidos completos = 33,33%.
As tabelas mostram entregas realizadas e datas, não atendimento imediato do estoque. São aproximações de atendimento; lagerservicegrad exato exige saber o que saiu imediatamente do estoque. Entrega pontual e completa é outro indicador: só o pedido 99777 cumpre ambos na amostra. Não confunda a amostra com os 60% informados para a empresa.
Estoque americano oculto aumenta capital imobilizado, obsolescência e sinais falsos de demanda. Compartilhe vendas/estoques reais e trabalhe com um plano comum.''','answer')
S(a,T('2.2 · Bloodscale A/S','2.2 · Bloodscale A/S','2.2 · Bloodscale A/S'),
'''Bloodscale producerer måleudstyr i Danmark og England. Omsætning nær 800 mio. kr.; 550 ansatte, heraf 75 i engelsk montage. Lead time er steget fra 3 til 5 uger; kunder og største konkurrent arbejder med 2 uger. Lager er steget ca. 30 %. Egne lastbiler kører delvist tomme. England bestiller skjult 10–15 % ekstra.
Måned | Bestilt | Rettidigt leveret
Januar | 2600 | 2400
Februar | 3000 | 2750
Marts | 2700 | 2700
April | 1000 | 980
Maj | 1200 | 600
Juni | 1500 | 1250
Juli | 1700 | 1000
August | 500 | 470
September | 600 | 450
Oktober | 670 | 580
November | 560 | 500
December | 700 | 500
Lagerdata i mio. kr. (værdi / kvartalets forbrug): råvarer 45/11, 50/12, 55/15, 60/17; halvfabrikata 50/18, 62/21, 69/25, 75/26; færdigvarer 85/40, 95/45, 100/55, 110/60.
1. Forklar udviklingen i logistisk effektivitet. 2. Foreslå forbedringer.''',
'''Bloodscale produces measuring equipment in Denmark and England. Revenue nearly DKK 800m; 550 staff, including 75 assembling in England. Lead time rises from 3 to 5 weeks; customers and the main competitor use 2 weeks. Stock rises about 30%. Own trucks run partly empty. England secretly orders 10–15% extra.
Month | Ordered | Delivered on time
January | 2600 | 2400
February | 3000 | 2750
March | 2700 | 2700
April | 1000 | 980
May | 1200 | 600
June | 1500 | 1250
July | 1700 | 1000
August | 500 | 470
September | 600 | 450
October | 670 | 580
November | 560 | 500
December | 700 | 500
Quarterly inventory data in DKK m (value / quarter consumption): raw materials 45/11, 50/12, 55/15, 60/17; semi-finished 50/18, 62/21, 69/25, 75/26; finished goods 85/40, 95/45, 100/55, 110/60.
1. Explain changing logistics efficiency. 2. Propose improvements.''',
'''Bloodscale produz equipamentos de medição na Dinamarca e Inglaterra. Faturamento próximo de DKK 800 milhões; 550 pessoas, 75 na montagem inglesa. Lead time sobe de 3 para 5 semanas; clientes e concorrente principal trabalham com 2. Estoque cresce cerca de 30%. Caminhões próprios viajam parcialmente vazios. A Inglaterra pede secretamente 10–15% a mais.
Mês | Pedido | Entregue no prazo
Janeiro | 2600 | 2400
Fevereiro | 3000 | 2750
Março | 2700 | 2700
Abril | 1000 | 980
Maio | 1200 | 600
Junho | 1500 | 1250
Julho | 1700 | 1000
Agosto | 500 | 470
Setembro | 600 | 450
Outubro | 670 | 580
Novembro | 560 | 500
Dezembro | 700 | 500
Dados trimestrais em milhões DKK (valor / consumo do trimestre): matérias-primas 45/11, 50/12, 55/15, 60/17; semiacabados 50/18, 62/21, 69/25, 75/26; acabados 85/40, 95/45, 100/55, 110/60.
1. Explique a evolução da eficiência logística. 2. Proponha melhorias.''','task')
S(a,T('2.2 · analyse','2.2 · analysis','2.2 · análise'),
'''Årets bestilte antal = 16.730; rettidigt leveret = 14.180. Vægtet rettidighed = 84,76 % af bestilte enheder. Månedstal er ca. 92,31; 91,67; 100; 98; 50; 83,33; 58,82; 94; 75; 86,57; 89,29; 71,43 %. Brug ikke et simpelt gennemsnit af månedsprocenterne som årsresultat.
Casefortællingen nævner 75 %. Det stemmer ikke med den vægtede tabelberegning; angiv datagrundlaget i din besvarelse.
Samlet lager stiger fra 180 til 245 mio. kr. i tabellen: 36,11 %. Det er ikke præcis casefortællingens ca. 30 %. Samlet kvartalsforbrug stiger fra 69 til 103. Større lager og længere leveringstid viser, at mere lager ikke nødvendigvis er det rigtige lager.
Årets forbrug = 345 mio. kr. Gennemsnit af de fire kvartalslagre = (180 + 207 + 224 + 245)/4 = 214. Estimeret årsomsætningshastighed = 345/214 = 1,61. Det er en approximation, fordi åbningslager og daglige gennemsnit mangler.
Forbedringer: fælles salgs- og kapacitetsplan; synlige lagre i begge lande; find flaskehalse og reducer partistørrelser; aftal realistiske leveringsdatoer; saml transporter med planlagte afgange uden at bryde kundeløfter.''',
'''Annual ordered units = 16,730; on-time units = 14,180. Weighted punctuality = 84.76% of ordered units. Monthly percentages are about 92.31, 91.67, 100, 98, 50, 83.33, 58.82, 94, 75, 86.57, 89.29 and 71.43. Do not average these percentages unweighted.
The narrative says 75%, which does not match the weighted table result. State which data you use.
Table stock rises from DKK 180m to 245m: 36.11%, rather than exactly the narrative’s roughly 30%. Quarterly consumption rises from 69 to 103. More stock is not necessarily the right stock.
Annual consumption = DKK 345m. Average of four quarter-end stocks = (180 + 207 + 224 + 245)/4 = 214. Estimated annual omsætningshastighed = 345/214 = 1.61. This is approximate: opening stock and daily averages are absent.
Improvements: joint sales/capacity planning; visibility of both countries’ stocks; address bottlenecks and batch sizes; realistic promises; planned consolidated transport consistent with delivery commitments.''',
'''Total anual pedido = 16.730 unidades; no prazo = 14.180. Pontualidade ponderada = 84,76% das unidades pedidas. Percentuais mensais aproximados: 92,31; 91,67; 100; 98; 50; 83,33; 58,82; 94; 75; 86,57; 89,29; 71,43%. Não faça média simples dos percentuais para obter o ano.
A narrativa informa 75%, diferente do resultado ponderado da tabela. Declare a base usada.
O estoque da tabela passa de DKK 180 para 245 milhões: 36,11%, não exatamente os cerca de 30% da narrativa. O consumo trimestral sobe de 69 para 103. Mais estoque não significa estoque correto.
Consumo anual = DKK 345 milhões. Média dos quatro saldos trimestrais = (180 + 207 + 224 + 245)/4 = 214. Omsætningshastighed anual estimado = 345/214 = 1,61. É aproximação: faltam estoque inicial e média diária.
Melhorias: planejamento conjunto de vendas/capacidade; visibilidade dos estoques; resolver gargalos e lotes; prazos realistas; consolidar viagens planejadas respeitando os compromissos.''','answer')
S(a,T('2.3 · Dancab A/S','2.3 · Dancab A/S','2.3 · Dancab A/S'),
'''Dancab fremstiller højttalerkabinetter på tre fabrikker i Danmark, Spanien og Australien. 550 ansatte, heraf 280 i produktion. 80 % eksport via 20 salgsselskaber. Lager og leveringstid stiger, mens overskud og afkastningsgrad falder.
2017-tal i mio. kr.: anlægsaktiver 400, lager 300, debitorer 35, likvider 10, omsætning 900, materialer 240, løn 90, kapacitetsomkostninger 350.
Mål: salg +15 %, lager −50 %, løn −5 %, materialepriser −12 %.
1. Forklar effektiviteten. 2. Hvorfor kan lageret stige? 3. Beregn forbedringen i afkastningsgrad, hvis målene realiseres.''',
'''Dancab makes loudspeaker cabinets in Denmark, Spain and Australia. It employs 550 people, 280 in production, and exports 80% through 20 sales companies. Stock and lead time rise as profit and afkastningsgrad fall.
2017 figures, DKK m: fixed assets 400, inventory 300, receivables 35, cash 10, revenue 900, materials 240, wages 90, capacity costs 350.
Targets: sales +15%, stock −50%, wages −5%, material prices −12%.
1. Explain efficiency. 2. Why might stock rise? 3. Calculate the improvement in afkastningsgrad if the targets are achieved.''',
'''Dancab fabrica gabinetes de caixas acústicas na Dinamarca, Espanha e Austrália. Tem 550 funcionários, 280 na produção; exporta 80% por 20 subsidiárias. Estoque e prazo sobem, lucro e afkastningsgrad caem.
Dados de 2017, milhões DKK: imobilizado 400, estoque 300, recebíveis 35, caixa 10, faturamento 900, materiais 240, salários 90, custos de capacidade 350.
Metas: vendas +15%, estoque −50%, salários −5%, preço dos materiais −12%.
1. Explique a eficiência. 2. Por que o estoque pode subir? 3. Calcule a melhoria do afkastningsgrad com as metas realizadas.''','task')
S(a,T('2.3 · resultat og antagelser','2.3 · result and assumptions','2.3 · resultado e premissas'),
'''Før: resultat = 900 − 240 − 90 − 350 = 220 mio. kr. Aktiver = 400 + 300 + 35 + 10 = 745. Afkastningsgrad = 220/745 × 100 = 29,53 %.
En simpel målopfyldelsesmodel: omsætning 1.035; materialer 211,2; løn 85,5; kapacitet 350. Resultat 388,3. Aktiver 595, hvis 150 i frigivet lagerkapital trækkes ud af virksomheden. Afkastningsgrad 65,26 %: +35,73 procentpoint eller +121,0 % relativt.
Men salgsvækst kan kræve flere materialer og timer. Hvis materialeforbrug skalerer med +15 % og pris falder 12 %, bliver materialer 242,88. Hvis løn også skalerer +15 % før besparelsen, bliver løn 98,325. Resultat = 343,795. Med aktiver 595 bliver afkastningsgrad 57,78 %.
Hvis frigivet kapital bliver stående som likvider, falder de samlede aktiver ikke automatisk. Afklar derfor med læreren, hvilken model der forventes. De simple måltal alene angiver ikke alle forudsætninger.
Mulige årsager til lagerstigning: store serier, langsomme varer, usikre prognoser, skjulte buffere og flaskehalse. Ensidige indkøbsbesparelser kan øge lager og leveringstid.''',
'''Before: profit = 900 − 240 − 90 − 350 = DKK 220m. Assets = 400 + 300 + 35 + 10 = 745. Afkastningsgrad = 220/745 × 100 = 29.53%.
Simple target model: revenue 1,035; materials 211.2; wages 85.5; capacity 350. Profit 388.3. Assets 595 if the 150 released from stock leaves the business. Return = 65.26%: +35.73 percentage points or +121.0% relatively.
But higher sales may require more inputs. Scaling material use by +15% before the 12% price cut gives 242.88. Scaling wages by +15% before the 5% saving gives 98.325. Profit = 343.795; with assets 595, return = 57.78%.
If released funds remain as cash, total assets do not automatically fall. Ask which model the teacher expects: the targets do not specify every assumption.
Possible stock drivers: large batches, slow movers, poor forecasts, hidden buffers and bottlenecks. Purchase-price savings alone can increase stock and lead time.''',
'''Antes: resultado = 900 − 240 − 90 − 350 = DKK 220 milhões. Ativos = 400 + 300 + 35 + 10 = 745. Afkastningsgrad = 220/745 × 100 = 29,53%.
Modelo simples de metas: faturamento 1.035; materiais 211,2; salários 85,5; capacidade 350. Resultado 388,3. Ativos 595, se os 150 liberados do estoque saírem da empresa. Retorno 65,26%: +35,73 pontos percentuais ou +121,0% relativos.
Mas vender mais pode exigir mais insumos. Aumentando consumo em 15% antes da redução de preço de 12%, materiais = 242,88. Escalando salários em 15% antes da economia de 5%, salários = 98,325. Resultado = 343,795; com ativos 595, retorno = 57,78%.
Se o capital liberado continuar no caixa, os ativos totais não caem automaticamente. Confirme o modelo esperado pelo professor: as metas não definem todas as premissas.
Causas possíveis do estoque: lotes grandes, itens lentos, previsão fraca, reservas ocultas e gargalos. Economizar apenas no preço de compra pode elevar estoque e prazo.''','answer')
S(a,T('2.4 · skadestue','2.4 · emergency department','2.4 · pronto-socorro'),
'''Beskriv logistisk effektivitet i en skadestue efter lærebogens ti punkter og underpunkter. Ingen vurdering eller tal skal med. Eksempel: leveringstid fra første modtagelse til færdig behandling.
Figur 2.1 på side 33 er ikke med i ZIP-filen. Brug den, hvis læreren udleverer den; nedenstående er en fagligt tilsvarende arbejdsmodel, ikke en ordret gengivelse af den manglende figur.''',
'''Describe logistics efficiency in an emergency department using the textbook’s ten points/subpoints. Do not include scores or figures. Example: time from arrival to completed treatment.
Figure 2.1 on page 33 is absent from the ZIP. Use it if supplied by the teacher. The following is an equivalent working model, not a reproduction of the missing figure.''',
'''Descreva a eficiência logística de um pronto-socorro pelos dez pontos e subpontos do livro. Não inclua notas nem números. Exemplo: tempo entre recebimento e conclusão do atendimento.
A figura 2.1 da página 33 não veio no ZIP. Use-a quando fornecida pelo professor. A proposta abaixo é um modelo equivalente, não uma reprodução da figura ausente.''','task')
S(a,T('2.4 · arbejdsmodel','2.4 · working model','2.4 · modelo de apoio'),
'''1. Leveringstid: registrering, triage, undersøgelse, behandling og udskrivning.
2. Lagerservicegrad: tilgængelighed af nødvendige lægemidler og materialer.
3. Leveringsoverholdelse: gennemførelse af planlagte undersøgelser og behandlinger som aftalt.
4. Leveringsfleksibilitet: tilpasning af personale, rum og udstyr til ændrede behov.
5. Leveringsinformation: information til patienten og koordinering mellem afdelinger.
6. Lageromkostninger: opbevaring, køling, svind og kapital i materialer.
7. Transportomkostninger: flytning af patienter, prøver og udstyr.
8. Emballage og håndtering: sterile pakninger og sikker håndtering.
9. Administration: registrering, journaler og planlægning.
10. Mangelomkostninger: ekstra koordinering og hasteanskaffelser ved manglende ressourcer.
Dette er en beskrivelse af processer, ikke en vurdering af behandling eller sundhedsfaglige prioriteringer.''',
'''1. Leveringstid: registration, triage, examination, treatment and discharge.
2. Lagerservicegrad: availability of required medicines/materials.
3. Leveringsoverholdelse: planned examinations/treatments carried out as agreed.
4. Leveringsfleksibilitet: adapting staff, rooms and equipment to changing needs.
5. Leveringsinformation: patient updates and interdepartment coordination.
6. Lageromkostninger: storage, refrigeration, shrinkage and tied-up capital.
7. Transportomkostninger: moving patients, samples and equipment.
8. Packaging/handling: sterile packs and safe handling.
9. Administration: records and planning.
10. Mangelomkostninger: extra coordination and emergency procurement when resources are absent.
This describes processes, not clinical decisions or medical prioritisation.''',
'''1. Leveringstid: registro, triagem, exame, tratamento e alta.
2. Lagerservicegrad: disponibilidade dos medicamentos e materiais necessários.
3. Leveringsoverholdelse: exames/tratamentos planejados realizados conforme o combinado.
4. Leveringsfleksibilitet: adaptar equipe, salas e equipamentos à demanda.
5. Leveringsinformation: informar o paciente e coordenar os setores.
6. Lageromkostninger: armazenagem, refrigeração, perdas e capital em materiais.
7. Transportomkostninger: deslocar pacientes, amostras e equipamentos.
8. Embalagem/manuseio: materiais estéreis e manejo seguro.
9. Administração: registros, prontuários e planejamento.
10. Mangelomkostninger: coordenação extra e compras emergenciais por falta de recursos.
É descrição de processos, não avaliação de decisões ou prioridades clínicas.''','answer')
S(a,T('2.5 · Nomeco','2.5 · Nomeco','2.5 · Nomeco'),
'''Den historiske case beskriver en medicinalgrossist med ca. 600 ansatte, 300 apoteker, 500 leverandører, 16.000 varenumre, fire lagerførende filialer og ca. 500 mio. kr. i lager. Et integreret IT-system muliggør hurtig bestilling og op til tre daglige leveringer. Apoteker, der er tæt integreret, har høje omstillingsomkostninger ved leverandørskift.
Kæden er medicinalproducent → dansk datterselskab/import → grossist → apotek → forbruger.
1. Diskutér konkurrence ved en hypotetisk fuld liberalisering. 2. Hvilke aktiviteter bør apoteker prioritere for at overleve? Opgaven handler om casens scenarie, ikke den aktuelle lovgivning.''',
'''The historical case describes a medicine wholesaler with about 600 staff, 300 pharmacies, 500 suppliers, 16,000 articles, four stocking branches and DKK 500m inventory. Integrated IT supports rapid orders and up to three daily deliveries. Closely integrated pharmacies face high supplier-switching costs.
Chain: medicine producer → Danish subsidiary/importer → wholesaler → pharmacy → consumer.
1. Discuss competition under hypothetical full liberalisation. 2. Which activities should pharmacies prioritise? This is the case scenario, not a statement of current law.''',
'''O caso histórico apresenta um distribuidor farmacêutico com cerca de 600 funcionários, 300 farmácias, 500 fornecedores, 16.000 itens, quatro filiais com estoque e DKK 500 milhões armazenados. TI integrada permite pedidos rápidos e até três entregas diárias. Farmácias fortemente integradas enfrentam alto custo para trocar de fornecedor.
Cadeia: fabricante → subsidiária/importador dinamarquês → atacadista → farmácia → consumidor.
1. Discuta a concorrência em uma liberalização total hipotética. 2. Quais atividades as farmácias deveriam priorizar? É o cenário do caso, não uma afirmação sobre a legislação atual.''','task')
S(a,T('2.5 · argumentation','2.5 · discussion guide','2.5 · guia de argumentação'),
'''Nye detailkanaler kan øge prispresset og gøre bekvemmelighed og tilgængelighed vigtigere. Producenter kan få flere salgskanaler; grossisten skal bevise sin værdi gennem sortiment, sikker distribution, data og effektivitet. Apoteker kan møde konkurrence på standardvarer, mens professionel rådgivning, tillid, service og relevant sortiment kan differentiere dem.
Apoteket bør prioritere indkøb/lagerstyring, præcis udlevering, kvalificeret kundeservice og en nem bestillings- og afhentningsproces. Diskutér også afhængighed af grossistens IT og omkostningen ved at skifte. Konkurrence betyder ikke, at kvalitet og sporbarhed kan ignoreres.''',
'''New retail channels may increase price pressure and the importance of convenience/availability. Producers gain channels; wholesalers must demonstrate value through assortment, reliable distribution, data and efficiency. Pharmacies may face standard-product competition while differentiating through professional advice, trust, service and relevant assortment.
Prioritise purchasing/stock control, accurate dispensing, qualified customer service and easy ordering/collection. Discuss dependence on wholesaler IT and switching costs. Competition does not remove quality or traceability needs.''',
'''Novos canais podem aumentar a pressão por preço e a importância de conveniência/disponibilidade. Fabricantes ganham canais; o atacadista precisa demonstrar valor por sortimento, distribuição confiável, dados e eficiência. Farmácias podem enfrentar concorrência em itens padronizados e se diferenciar por orientação profissional, confiança, serviço e sortimento relevante.
Priorize compras/estoque, entrega precisa, atendimento qualificado e facilidade de pedir/retirar. Discuta dependência da TI do atacadista e custo de troca. Concorrência não elimina qualidade e rastreabilidade.''','answer')
S(a,T('2.6 · Autoservice','2.6 · Autoservice','2.6 · Autoservice'),
'''Autoservice lover reparation af høj kvalitet og kort ventetid, også uden tidsbestilling. Kæden er komponentleverandør → reservedelsproducent → importør → lokal forhandler → værksted.
Forhandler og importør prioriterer kort leveringstid. Producentens indkøb måles på besparelser, og komponentleverandøren producerer store serier for høj produktivitet.
1. Karakterisér aktørerne. 2. Find order winners og order qualifiers hos Autoservice. 3. Find dem hos komponentleverandøren. 4. Forklar følgerne af de forskellige logistiske mål.''',
'''Autoservice promises high-quality repairs and short waiting times, including walk-ins. Chain: component supplier → parts manufacturer → importer → local dealer → workshop.
Dealer/importer prioritise speed. Manufacturer purchasing is measured on savings; component suppliers use large batches for productivity.
1. Characterise the actors. 2. Identify order winners and qualifiers for Autoservice. 3. Identify them for component suppliers. 4. Explain consequences of conflicting logistics objectives.''',
'''Autoservice promete reparos de qualidade e pouca espera, mesmo sem agendamento. Cadeia: fornecedor de componentes → fabricante de peças → importador → revendedor local → oficina.
Revendedor/importador priorizam rapidez. Compras do fabricante é medido pela economia; fornecedores produzem lotes grandes para ganhar produtividade.
1. Caracterize os participantes. 2. Identifique order winners e qualifiers da oficina. 3. Identifique os do fornecedor de componentes. 4. Explique os efeitos de objetivos logísticos diferentes.''','task')
S(a,T('2.6 · en sammenhængende kæde','2.6 · aligning the chain','2.6 · alinhando a cadeia'),
'''Aktørerne er henholdsvis industriel underleverandør, producent, import-/engrosled, handelsvirksomhed og servicevirksomhed.
Autoservice: kvalitet og godkendt kompatibilitet er sandsynlige order qualifiers; meget kort ventetid og adgang uden booking er sandsynlige order winners. Den præcise klassifikation afhænger af kundernes minimumskrav og konkurrenterne.
Komponentleverandøren konkurrerer sandsynligvis på pris og produktivitet, med specifikation og stabil kvalitet som minimumskrav.
Store serier og lange omstillingstider upstream kan give mangel downstream og dermed længere ventetid for bilkunden. Brug fælles måltal, faktiske forbrugsdata, passende lager på kritiske dele og aftaler om genopfyldning.''',
'''Actors: industrial subcontractor, manufacturer, importer/wholesaler, trading business and service business.
Autoservice: quality and approved compatibility are likely order qualifiers; very short waits and walk-in access are likely order winners. Classification depends on customer minimum requirements and competitors.
Component suppliers likely compete on price/productivity, with specification and consistent quality as minimum requirements.
Large upstream batches and changeover times can create downstream shortages and longer customer waits. Use shared metrics, actual consumption data, appropriate critical-parts stock and replenishment agreements.''',
'''Participantes: subfornecedor industrial, fabricante, importador/atacadista, empresa comercial e prestadora de serviço.
Autoservice: qualidade e compatibilidade aprovada são prováveis order qualifiers; espera muito curta e atendimento sem agendamento são prováveis order winners. A classificação depende do mínimo exigido pelo cliente e dos concorrentes.
O fornecedor de componentes provavelmente compete por preço/produtividade, tendo especificação e qualidade estável como requisitos mínimos.
Lotes grandes e tempos de preparação upstream podem causar faltas downstream e espera do cliente. Use indicadores comuns, consumo real, estoque adequado de peças críticas e acordos de reposição.''','answer')
S(a,T('2.7 · CoolIt · fortsættelse mangler','2.7 · CoolIt · continuation missing','2.7 · CoolIt · continuação ausente'),
'''Den sidste side begynder kun casen: CoolIt A/S fremstiller køleskabe til butikskæder i Danmark, Tyskland og Sverige. Virksomheden blev grundlagt i 2008 og har 80 medarbejdere i casen.
Resten af casen og spørgsmålene er ikke med i PDF’en. Der kan ikke beregnes eller gives en konkret løsning uden næste side. Bed læreren om fortsættelsen.''',
'''The last page only starts the case: CoolIt makes refrigerators for retail chains in Denmark, Germany and Sweden. Founded in 2008, it employs 80 people in the case.
The remaining case and questions are absent. A specific answer or calculation requires the next page. Ask the teacher for the continuation.''',
'''A última página apenas inicia o caso: CoolIt fabrica refrigeradores para redes da Dinamarca, Alemanha e Suécia. Fundada em 2008, tem 80 funcionários no caso.
O restante e as perguntas não estão no PDF. Não é possível calcular ou responder especificamente sem a página seguinte. Peça a continuação ao professor.''','notice')

a=page(5,T('Opgaveoversigt','Assignment overview','Resumo das atividades'),T('Denne tekstfil henviser til cases og bogopgaver, som allerede har egne undersider.','This text file refers to cases and textbook exercises with their own pages.','Este arquivo remete aos casos e exercícios do livro que têm páginas próprias.'))
S(a,T('Det skal du arbejde med','What to work on','O que fazer'),
'''- Arbejd med cases om de syv logistikmål i kapitel 1.
- Arbejd med bogens opgaver om logistisk effektivitet i dette kapitel.
Begynd med definitionerne. Markér tal og aftaler. Vis formel, indsatte tal, resultat og enhed. Afslut med én sætning om, hvad resultatet betyder.''',
'''- Work on the seven-objective cases in chapter 1.
- Work on the textbook logistics-efficiency cases in this chapter.
Start with definitions. Mark figures and agreements. Show the formula, substituted values, result and unit. Finish with one sentence explaining its meaning.''',
'''- Faça os casos dos sete objetivos no capítulo 1.
- Faça os exercícios do livro sobre eficiência logística neste capítulo.
Comece pelas definições. Marque números e acordos. Mostre fórmula, valores, resultado e unidade. Termine com uma frase interpretando o resultado.''')
a=page(6,T('Virksomhedsbesøg · HYDREMA','Company visit · HYDREMA','Visita técnica · HYDREMA'),T('Forbind teori med de processer, du kan observere på besøget.','Connect theory with processes you can observe during the visit.','Relacione a teoria aos processos observáveis na visita.'))
S(a,T('Oplysninger fra invitationen','Details from the invitation','Informações do convite'),
'''Invitationen angiver Gl. Kirkevej 16, 9530 Støvring. Mødetid ca. kl. 8.20, klar til samling kl. 8.30. Allan Mølgaard fra Marketing tager imod, efterfulgt af præsentation og besøg i produktion, lager og andre afdelinger.
Der er ingen besøgsdato i tekstfilen. Bekræft dato, mødetid, kontaktperson, transport og sikkerhedsudstyr med skolen. Oplysningerne er fra materialet, ikke en ny booking.
Materialet beskriver HYDREMA som producent, sælger og servicevirksomhed for entreprenørmaskiner, blandt andet dumpere, rendegravere, gravemaskiner og maskiner til bane/forsvar. Formuleringen om 50 års historie er historisk og skal ikke bruges som virksomhedens aktuelle alder.''',
'''The invitation lists Gl. Kirkevej 16, 9530 Støvring. Meet around 08:20, ready at 08:30. Allan Mølgaard from Marketing welcomes the group, followed by a presentation and visits to production, lager and other departments.
The text contains no visit date. Confirm date, time, contact, travel and safety equipment with the school. These are source details, not a new booking.
The material describes HYDREMA as a manufacturer, seller and service provider for construction equipment, including dumpers, backhoe loaders, excavators and rail/defence equipment. Its reference to a 50-year history is historical, not the company’s current age.''',
'''O convite informa Gl. Kirkevej 16, 9530 Støvring. Encontro por volta de 8h20, prontos às 8h30. Allan Mølgaard, do Marketing, recebe o grupo; depois há apresentação e visita à produção, lager e outros setores.
O TXT não informa a data. Confirme data, horário, contato, transporte e equipamentos de segurança com a escola. São dados do material, não uma nova reserva.
O material apresenta a HYDREMA como fabricante, vendedora e prestadora de serviços de máquinas de construção, incluindo dumpers, retroescavadeiras, escavadeiras e equipamentos ferroviários/de defesa. A referência a 50 anos de história é histórica, não a idade atual.''')
S(a,T('Spørgsmål du kan tage med','Questions to take along','Perguntas para levar'),
'''- Hvordan planlægger I indkøb og levering af komponenter?
- Hvordan registrerer I varer ved varemodtagelse?
- Hvor kan der opstå flaskehalse mellem lager og produktion?
- Hvordan måler I leveringstid og leveringsoverholdelse?
- Hvordan sikrer I kvalitet og sporbarhed?
- Hvad gør I, hvis en kritisk komponent mangler?
- Hvilke opgaver udfører I selv, og hvilke er outsourcede?
Efter besøget: skriv tre observationer, to forbindelser til teorien og ét spørgsmål, du stadig har. Sammenlign en produktionsvirksomhed med dit arbejde i et IKEA-varehus.''',
'''- How do you plan component indkøb and deliveries?
- How do you register goods at varemodtagelse?
- Where can bottlenecks arise between lager and production?
- How do you measure leveringstid and leveringsoverholdelse?
- How do you ensure quality and traceability?
- What happens when a critical component is missing?
- Which activities are internal and which are outsourced?
Afterwards, write three observations, two links to theory and one remaining question. Compare a manufacturing business with your IKEA store work.''',
'''- Como planejam indkøb e entrega de componentes?
- Como registram produtos na varemodtagelse?
- Onde podem surgir gargalos entre lager e produção?
- Como medem leveringstid e leveringsoverholdelse?
- Como garantem qualidade e rastreabilidade?
- O que fazem quando falta um componente crítico?
- Quais atividades são internas e quais terceirizadas?
Depois, escreva três observações, duas relações com a teoria e uma dúvida restante. Compare uma fabricante com seu trabalho no varejo IKEA.''','task')

a=page(7,T('Værdikæde og internationalisering','Value chain and internationalisation','Cadeia de valor e internacionalização'),T('Lær Porters model trin for trin, og anvend den på en vare, du kender.','Learn Porter’s model step by step and apply it to a product you know.','Aprenda o modelo de Porter passo a passo e aplique-o a um produto que você conhece.'))
a['videos']=['e1XaT__IAxo']
S(a,T('Sådan bruger du lektionen','How to use the lesson','Como usar a aula'),
'''Læs lektionen nedenfor. Prøv derefter at nævne én aktivitet, der flytter en ordre fremad, og én, som støtter mange ordrer. Brug f.eks. en lampe: at pakke den til kunden er en primær aktivitet. At oplære medarbejderne i pakning er en støtteaktivitet.''',
'''Read the lesson below. Then name one activity that moves an order forward and another that supports many orders. Use a lamp: packing it for the customer is a primary activity. Training employees to pack is a support activity.''',
'''Leia a aula abaixo. Depois cite uma atividade que faz um pedido avançar e outra que dá suporte a muitos pedidos. Use uma luminária: embalar para o cliente é atividade primária. Ensinar a equipe a embalar é atividade de apoio.''')

a=page(8,T('Værdikæden og make or buy','The value chain and make or buy','Cadeia de valor e make or buy'),T('Find de aktiviteter, der skaber værdi, og de forbindelser, der gør hele processen bedre.','Identify value-creating activities and the links that improve the whole process.','Identifique as atividades que geram valor e as conexões que melhoram o processo completo.'))
S(a,T('Fem primære aktiviteter','Five primary activities','Cinco atividades primárias'),
'''Aktivitet | Eksempler fra materialet
Indgående logistik | Modtagelse, losning, kontrol, registrering og placering af varer.
Produktion / operationer | Fremstilling, montage, ompakning, etikettering, kitting og kvalitetskontrol.
Udgående logistik | Pluk, pak, lastning, transport, tracking og leveringsdokumentation.
Marketing og salg | Skabe efterspørgsel, tage imod ordrer, aftale pris og realistisk leveringsservice.
Service | Retur, reparation, garanti, reservedele, installation og hjælp efter køb.
I en handelsvirksomhed som et varehus kan operationer være klargøring, håndtering og udstilling, ikke nødvendigvis fremstilling. Cross-docking flytter varer videre med minimal lagring; konsolidering samler forsendelser. De er logistiske procesvalg, ikke altid produktion.''',
'''Activity | Examples from the material
Inbound logistics (Indgående logistik) | Receiving, unloading, inspection, registration and put-away.
Production / operations | Manufacturing, assembly, repacking, labelling, kitting and checks.
Outbound logistics (Udgående logistik) | Pluk, pak, loading, transport, tracking and delivery documentation.
Marketing and sales | Create demand, take orders, agree prices and realistic service.
Service | Returns, repairs, warranty, parts, installation and post-sale support.
In a retailer, operations can mean preparation, handling and displays rather than manufacturing. Cross-docking forwards goods with minimal storage; consolidation combines shipments. These are logistics choices, not necessarily production.''',
'''Atividade | Exemplos do material
Logística de entrada (Indgående logistik) | Receber, descarregar, conferir, registrar e endereçar produtos.
Produção / operações | Fabricar, montar, reembalar, etiquetar, formar kits e conferir qualidade.
Logística de saída (Udgående logistik) | Pluk, pak, carregamento, transporte, rastreamento e comprovantes.
Marketing e vendas | Gerar demanda, receber pedidos, combinar preço e serviço viável.
Service | Devoluções, reparos, garantia, peças, instalação e suporte pós-venda.
No varejo, operações podem ser preparação, manuseio e exposição, sem fabricação. Cross-docking encaminha produtos quase sem armazenagem; consolidação reúne cargas. São escolhas logísticas, não necessariamente produção.''')
S(a,T('Fire støtteaktiviteter','Four support activities','Quatro atividades de apoio'),
'''- Infrastruktur: ledelse, økonomi, planlægning, IT, WMS, ruteplanlægning og KPI-opfølgning.
- HR: rekruttering, uddannelse, truckcertifikater, samarbejde og arbejdsmiljø.
- Teknologiudvikling: scannere, automatisering, robotter, sensorer og analyse af efterspørgsel.
- Indkøb: anskaffelse af varer og ydelser, emballage, transport, udstyr og IT.
Indkøb i Porter-modellen er en støtteaktivitet; fysisk modtagelse er indgående logistik. Afdelingen kan bidrage til begge, men aktiviteternes funktion er forskellig.''',
'''- Infrastructure (Infrastruktur): management, finance, planning, IT, WMS, routes and KPI follow-up.
- HR: recruitment, training, truck certification, cooperation and workplace safety.
- Technology development: scanners, automation, robots, sensors and demand analysis.
- Purchasing (Indkøb): obtaining goods/services, packaging, transport, equipment and IT.
Indkøb is a support activity in Porter’s model; physically receiving goods is indgående logistik. A department may contribute to both, but the activities serve different functions.''',
'''- Infraestrutura (Infrastruktur): gestão, finanças, planejamento, TI, WMS, rotas e indicadores.
- RH: recrutamento, treinamento, habilitação de empilhadeira, colaboração e segurança.
- Desenvolvimento tecnológico: scanners, automação, robôs, sensores e análise da demanda.
- Compras (Indkøb): adquirir bens/serviços, embalagem, transporte, equipamentos e TI.
No modelo de Porter, indkøb é apoio; receber fisicamente é indgående logistik. Um departamento pode contribuir com ambas, mas as funções são diferentes.''')
S(a,T('Hvad viser en analyse?','What does an analysis reveal?','O que a análise mostra?'),
'''Værdikæden kan vise, hvor kunden oplever mest værdi; hvor virksomheden er stærk eller svag; hvor omkostninger og flaskehalse opstår; og hvor der er mulighed for automatisering, koordinering eller outsourcing.
En konkurrencefordel kan komme fra lavere totalomkostning eller en forskel, kunden vil betale for. En lokal besparelse er ikke en forbedring, hvis den skaber større fejl og ventetid et andet sted.
Make or buy: Skal en aktivitet udføres internt eller købes hos en partner? Fjern aktiviteter uden værdi. Beskyt strategiske kompetencer. Sammenlign kapacitet, kvalitet, pris, leveringstid, dokumentation, afhængighed og totalomkostning, før du beslutter.''',
'''Værdikæden reveals where customers see value, strengths/weaknesses, costs, bottlenecks and opportunities for automation, coordination or outsourcing.
A competitive advantage can come from lower total costs or differentiation customers value. A local saving is not an improvement if it creates greater errors or waiting elsewhere.
Make or buy asks whether to perform an activity internally or buy it from a partner. Remove non-value-adding activities, protect strategic capabilities and compare capacity, quality, price, lead time, documentation, dependence and total cost.''',
'''Værdikæden mostra onde o cliente percebe valor, forças/fraquezas, custos, gargalos e oportunidades de automação, coordenação ou terceirização.
A vantagem competitiva pode vir de custo total menor ou diferenciação valorizada pelo cliente. Economizar em um setor não melhora o todo se cria mais erros ou espera em outro.
Make or buy pergunta se a atividade deve ser interna ou contratada. Elimine atividades sem valor, proteja competências estratégicas e compare capacidade, qualidade, preço, prazo, documentação, dependência e custo total.''')
S(a,T('Opgaver · din egen virksomhed','Assignments · your business','Tarefas · sua empresa'),
'''1. Lav en værdikædeanalyse af din virksomhed med generelt eller logistisk fokus. Fremlæg den.
2. Vis én konkret kundes ordre fra bestilling til efterservice. Beskriv vareflow og informationsflow.
3. Læs de to artikler. Diskutér aktiviteter eller produkter, som kunne udføres internt eller lægges ud. Begrund valget.''',
'''1. Analyse your company’s værdikæde from a general or logistics perspective and present it.
2. Follow one customer order from placement to after-sales. Explain goods and information flows.
3. Read both articles. Discuss activities/products to perform internally or outsource and justify your decision.''',
'''1. Analise a værdikæde da sua empresa com foco geral ou logístico e apresente.
2. Acompanhe um pedido da compra ao pós-venda. Explique os fluxos de mercadorias e informações.
3. Leia os dois artigos. Discuta atividades/produtos para realizar internamente ou terceirizar e justifique.''','task')
S(a,T('IKEA · eksempel, som skal tilpasses','IKEA · example to adapt','IKEA · exemplo para adaptar'),
'''Indgående: modtag og kontrollér kolli. Operationer: placér, genopfyld og gør varen klar. Udgående: pluk og udlever eller send kunden varen. Salg: produktinformation, pris og kundeaftale. Service: hjælp ved manglende dele og retur efter de lokale regler.
Støtte: HR uddanner i sikre løft og udstyr; IT forbinder ordre og lager; indkøb aftaler varer og transport; ledelsen følger kvalitet og service.
Overvej eksempelvis ekstern transport ved kapacitetsbehov. Behold kontrol over korrekte ordredata og kundeløfter. Det er et diskussionsforslag, ikke en beskrivelse af en bestemt IKEA-kontrakt.''',
'''Inbound: receive and inspect packages. Operations: store, replenish and prepare. Outbound: pick and hand over or dispatch. Sales: product information, pricing and agreements. Service: support for missing parts/returns under local procedures.
Support: HR trains safe handling; IT links orders/stock; purchasing contracts goods/transport; management follows quality/service.
External transport may help capacity. Retain control of accurate order data and delivery promises. This is a discussion example, not a claim about a particular IKEA contract.''',
'''Entrada: receber e conferir volumes. Operações: armazenar, repor e preparar. Saída: separar e entregar ou expedir. Vendas: informação do produto, preço e acordo. Serviço: peças faltantes e devolução conforme procedimento local.
Apoio: RH treina manuseio seguro; TI conecta pedido/estoque; compras contrata produtos/transporte; gestão acompanha qualidade/serviço.
Transporte externo pode ajudar a capacidade. Mantenha controle dos dados do pedido e promessas ao cliente. É exemplo de discussão, não descrição de um contrato específico da IKEA.''','answer')

a=page(9,T('Artikel · lav selv eller læg ud?','Article · make or outsource?','Artigo · produzir ou terceirizar?'),T('Einar Olsen, Valcon Sourcing · SCM.dk, 28. april 2008. Bearbejdet ud fra den vedlagte PDF.','Einar Olsen, Valcon Sourcing · SCM.dk, 28 April 2008. Adapted from the supplied PDF.','Einar Olsen, Valcon Sourcing · SCM.dk, 28 de abril de 2008. Adaptação do PDF fornecido.'))
a=page(10,T('Artikel · outsourcing og hjemtagning','Article · outsourcing and bringing production back','Artigo · terceirização e retorno da produção'),T('Amdi Hansen, PA Consulting Group · historisk artikel, vedlagt som PDF.','Amdi Hansen, PA Consulting Group · historical article supplied as PDF.','Amdi Hansen, PA Consulting Group · artigo histórico fornecido em PDF.'))
a=page(11,T('Beregninger til værdikæden','Value-chain calculations','Cálculos da cadeia de valor'),T('Vis altid aktivitetsfordeling, total og hvilken procentbase du bruger.','Always show activity costs, total and the percentage base.','Mostre custos por atividade, total e base de cada percentual.'))
S(a,T('Opgave 1 · LegetøjsFabrikken','Exercise 1 · LegetøjsFabrikken','Exercício 1 · LegetøjsFabrikken'),
'''En legetøjsbil bruger plast 45 kr., metal 95 kr., elektronik 120 kr. og maling/dekoration 40 kr. Produktion koster løn 150 kr. og maskiner/værktøj 50 kr. Udgående logistik 40 kr.; marketing/salg 20 kr.; service 10 kr.
Lav en grafisk fordeling på de fem primære aktiviteter. Beregn totalen og salgsmargin ved en pris på 800 kr. Materialerne grupperes i opgaven under indgående logistik; der er ikke oplyst særskilt modtagelsesomkostning.''',
'''One toy car uses plastic DKK 45, metal 95, electronics 120 and paint/decoration 40. Production labour is 150 and machines/tools 50. Udgående logistik costs 40, marketing/sales 20 and service 10.
Chart the five primary activities. Find total cost and sales margin at DKK 800. The exercise groups materials under indgående logistik; no separate receiving cost is specified.''',
'''Um carrinho usa plástico DKK 45, metal 95, eletrônica 120 e pintura/decoração 40. Produção: salários 150 e máquinas/ferramentas 50. Udgående logistik 40; marketing/vendas 20; serviço 10.
Faça um gráfico das cinco atividades, calcule total e margem de venda por DKK 800. A tarefa agrupa materiais em indgående logistik; não informa custo separado de recebimento.''','task')
S(a,T('Opgave 1 · omkostninger og margin','Exercise 1 · costs and margin','Exercício 1 · custos e margem'),
'''Aktivitet | Kr. | Andel af samlet kostpris
Indgående logistik / materialer | 300 | 52,63 %
Produktion | 200 | 35,09 %
Udgående logistik | 40 | 7,02 %
Marketing og salg | 20 | 3,51 %
Service | 10 | 1,75 %
I alt | 570 | 100 %
Fortjeneste = 800 − 570 = 230 kr. Salgsmargin = 230 / 800 × 100 = 28,75 %. Påslag på kostpris = 230 / 570 × 100 = 40,35 %. Margin og påslag har forskellig nævner.''',
'''Activity | DKK | Share of total cost
Indgående logistik / materials | 300 | 52.63%
Production | 200 | 35.09%
Udgående logistik | 40 | 7.02%
Marketing and sales | 20 | 3.51%
Service | 10 | 1.75%
Total | 570 | 100%
Profit = 800 − 570 = DKK 230. Sales margin = 230 / 800 × 100 = 28.75%. Markup on cost = 230 / 570 × 100 = 40.35%. The denominators differ.''',
'''Atividade | DKK | Parcela do custo total
Indgående logistik / materiais | 300 | 52,63%
Produção | 200 | 35,09%
Udgående logistik | 40 | 7,02%
Marketing e vendas | 20 | 3,51%
Serviço | 10 | 1,75%
Total | 570 | 100%
Lucro = 800 − 570 = DKK 230. Margem de venda = 230 / 800 × 100 = 28,75%. Acréscimo sobre custo = 230 / 570 × 100 = 40,35%. Os denominadores são diferentes.''','answer')
a['chart']={'section':1,'values':[300,200,40,20,10]}
S(a,T('Opgave 2 · GKL-køkkenet','Exercise 2 · the GKL kitchen','Exercício 2 · cozinha GKL'),
'''Standardkøkken: elementer 8.000 kr., hvidevarer 14.500 kr., sokler/øvrigt 4.200 kr. Produktion: samling 3.500 kr., maskiner 250 kr. Udgående: emballage 150 kr. og transport 350 kr. Marketing: reklame 200 kr. og tegning/opmåling 800 kr. Service/garanti 2.750 kr.
1. Beregn total og fortjeneste i kroner og procent ved salgspris 80.000 kr.
2. En tilpasning lægger 20.000 kr. til hvidevarer, 8.000 kr. til elementer og 2.000 kr. til øvrigt. For hver påbegyndt 5.000 kr. ekstra i indgående logistik stiger produktion med 1.000 kr. Service bliver 10 % af indgående + produktion + udgående logistik. Beregn alle fem aktiviteter.
3. Fortjenesten skal være mindst 150 % af samlede omkostninger. Find salgsprisen.
Her fortolkes tilpasningsbeløbene som tillæg. Hvis læreren mener nye totaler, skal beregningen ændres.''',
'''Standard kitchen: cabinets DKK 8,000, appliances 14,500, plinths/other 4,200. Production: assembly 3,500, machines 250. Outbound: packaging 150, transport 350. Marketing: advertising 200, drawings/measurement 800. Service/warranty 2,750.
1. Find total cost and profit in money/percentage at DKK 80,000 sales price.
2. Customisation adds 20,000 to appliances, 8,000 to cabinets and 2,000 to other items. Each started DKK 5,000 additional inbound cost adds DKK 1,000 production cost. Service becomes 10% of inbound + production + outbound. Calculate all five activities.
3. Profit must be at least 150% of total cost. Find the price.
Customisation figures are interpreted as additions. If the teacher means replacement totals, recalculate.''',
'''Cozinha padrão: módulos DKK 8.000, eletrodomésticos 14.500, rodapés/outros 4.200. Produção: montagem 3.500, máquinas 250. Saída: embalagem 150, transporte 350. Marketing: publicidade 200, desenho/medição 800. Serviço/garantia 2.750.
1. Calcule total e lucro em dinheiro/percentual com venda por DKK 80.000.
2. Personalização acrescenta 20.000 aos eletrodomésticos, 8.000 aos módulos e 2.000 aos demais. Cada DKK 5.000 adicionais iniciados na entrada aumenta produção em DKK 1.000. Serviço passa a 10% de entrada + produção + saída. Calcule as cinco atividades.
3. O lucro deve ser pelo menos 150% do custo total. Ache o preço.
Os valores de personalização são interpretados como acréscimos. Se o professor entender como novos totais, recalcule.''','task')
S(a,T('Opgave 2 · løsning med mellemregninger','Exercise 2 · worked solution','Exercício 2 · resolução detalhada'),
'''Aktivitet | Standard kr. | Tilpasset kr.
Indgående logistik | 26.700 | 56.700
Produktion | 3.750 | 9.750
Udgående logistik | 500 | 500
Marketing og salg | 1.000 | 1.000
Service | 2.750 | 6.695
I alt | 34.700 | 74.645
Standard: fortjeneste = 80.000 − 34.700 = 45.300 kr. Salgsmargin = 56,625 %. Påslag på kostpris = 130,55 %.
Tilpasning: indgående stiger med 30.000. Antal påbegyndte 5.000 = 6; produktion stiger 6.000. Service = (56.700 + 9.750 + 500) × 10 % = 6.695. Den nye service erstatter de 2.750 kr.; den lægges ikke oveni.
Pris med fortjeneste på 150 % af kostpris = 74.645 × (1 + 1,50) = 186.612,50 kr. Fortjeneste = 111.967,50 kr. Salgsmargin er 60 %, ikke 150 %. Der er ingen oplysning om momsbehandling; alle beløb sammenlignes på samme grundlag.''',
'''Activity | Standard DKK | Custom DKK
Indgående logistik | 26,700 | 56,700
Production | 3,750 | 9,750
Udgående logistik | 500 | 500
Marketing and sales | 1,000 | 1,000
Service | 2,750 | 6,695
Total | 34,700 | 74,645
Standard profit = 80,000 − 34,700 = DKK 45,300. Sales margin = 56.625%; markup on cost = 130.55%.
Custom: inbound rises 30,000. Six started increments of 5,000 add 6,000 production cost. Service = (56,700 + 9,750 + 500) × 10% = 6,695, replacing the old 2,750 rather than adding to it.
Price with profit at 150% of cost = 74,645 × (1 + 1.50) = DKK 186,612.50. Profit = 111,967.50. Sales margin is 60%, not 150%. VAT treatment is unspecified; compare all amounts on a consistent basis.''',
'''Atividade | Padrão DKK | Personalizado DKK
Indgående logistik | 26.700 | 56.700
Produção | 3.750 | 9.750
Udgående logistik | 500 | 500
Marketing e vendas | 1.000 | 1.000
Serviço | 2.750 | 6.695
Total | 34.700 | 74.645
Padrão: lucro = 80.000 − 34.700 = DKK 45.300. Margem de venda = 56,625%; acréscimo sobre custo = 130,55%.
Personalizado: entrada aumenta 30.000. São seis intervalos iniciados de 5.000, elevando produção em 6.000. Serviço = (56.700 + 9.750 + 500) × 10% = 6.695, substituindo os 2.750 antigos, não somando.
Preço com lucro de 150% do custo = 74.645 × (1 + 1,50) = DKK 186.612,50. Lucro = 111.967,50. Margem de venda é 60%, não 150%. Não há tratamento de IVA informado; compare os valores na mesma base.''','answer')

a=page(12,T('Supply Chain Management · grundlag','Supply Chain Management · fundamentals','Supply Chain Management · fundamentos'),T('En forsyningskæde er et netværk. SCM koordinerer processerne på tværs af virksomheder.','A forsyningskæde is a network. SCM coordinates processes across companies.','Uma forsyningskæde é uma rede. SCM coordena os processos entre as empresas.'))
a['videos']=['Bblo8_B32Co','w1Loz8IG73I']
S(a,T('Aktører og tre strømme','Participants and three flows','Participantes e três fluxos'),
'''Forsyningskæden kan omfatte råvareleverandører, komponentproducenter, producenter, grossister, transportører, lagre, detailhandel, offentlige kunder og slutbrugere. Virksomheder kan have flere roller, og kæden er ofte et netværk frem for en lige linje.
Vareflow går typisk mod kunden. Informationsflow går begge veje: ordrer, lager, prognoser og afvigelser. Betalingsflow går typisk den modsatte vej af varerne. Returvarer og genbrug giver også vareflow tilbage.
Upstream er mod leverandørerne; downstream er mod slutkunden. SCM søger en samlet fordel, ikke bare en afdelings lave omkostning. En underleverandør fremstiller efter en anden virksomheds krav eller som bidrag til dens produkt.''',
'''A forsyningskæde can include raw-material suppliers, component makers, manufacturers, wholesalers, carriers, warehouses, retailers, public customers and end users. Businesses can have several roles; the chain is usually a network.
Goods generally flow toward customers. Informationsflow is two-way: orders, stock, forecasts and exceptions. Payment generally flows opposite to goods. Returns and reuse also create reverse goods flows.
Upstream points toward suppliers; downstream toward end customers. SCM seeks whole-network value, beyond one department’s savings. A subcontractor supplies to another business’s specifications or contributes to its product.''',
'''Uma forsyningskæde pode incluir fornecedores de matérias-primas/componentes, fabricantes, atacadistas, transportadoras, depósitos, varejo, clientes públicos e consumidores. Uma empresa pode ter vários papéis; normalmente é uma rede.
Mercadorias geralmente seguem ao cliente. Informationsflow é bidirecional: pedidos, estoque, previsões e desvios. Pagamentos normalmente seguem no sentido oposto aos produtos. Devolução e reutilização criam fluxo reverso.
Upstream aponta para fornecedores; downstream para o consumidor. SCM busca valor para a rede, além da economia de um setor. Um subfornecedor atende às especificações de outra empresa ou contribui para o produto dela.''')
S(a,T('Effektiv eller responsiv?','Efficient or responsive?','Eficiente ou responsiva?'),
'''Valg | Effektiv forsyningskæde | Responsiv forsyningskæde
Primært mål | Lave samlede omkostninger | Hurtig reaktion på ændringer
Efterspørgsel | Relativt stabil og forudsigelig | Mere usikker, sæson- eller modepræget
Kapacitet | Høj udnyttelse | Buffer og fleksibilitet
Lager | Høj omsætningshastighed | Målrettet buffer, hvor det hjælper
Leverandørvalg | Pris og stabilitet | Reaktionsevne, kvalitet og service
Eksempel | Standard-T-shirt med få varianter | Modetøj med hyppige designændringer
Det er en forenklet model. Et stort lager er ikke automatisk responsivt. Placering, produktmix, leveringstid og fleksibilitet skal passe til kundens behov. Mismatch opstår fx, når ustabil efterspørgsel styres med meget lange, ufleksible serier.''',
'''Choice | Efficient supply chain (Effektiv forsyningskæde) | Responsive supply chain (Responsiv forsyningskæde)
Main goal | Low total cost | Rapid response to change
Demand | Relatively stable/predictable | Uncertain, seasonal or fashion-driven
Capacity | High utilisation | Buffer and flexibility
Stock | High omsætningshastighed | Targeted useful buffers
Supplier choice | Price and stability | Responsiveness, quality and service
Example | Standard T-shirt, few variants | Fashion with frequent design changes
This is simplified. A large inventory is not automatically responsive. Position, mix, lead time and flexibility must fit demand. Mismatch occurs when uncertain demand is served by very long inflexible batches.''',
'''Escolha | Cadeia eficiente (Effektiv forsyningskæde) | Cadeia responsiva (Responsiv forsyningskæde)
Objetivo | Baixo custo total | Reagir rapidamente a mudanças
Demanda | Estável/previsível | Incerta, sazonal ou de moda
Capacidade | Alta utilização | Reserva e flexibilidade
Estoque | Alta omsætningshastighed | Reservas direcionadas onde ajudam
Fornecedor | Preço e estabilidade | Reação, qualidade e serviço
Exemplo | Camiseta básica com poucas variantes | Moda com mudanças frequentes
É um modelo simplificado. Estoque grande não é automaticamente responsivo. Localização, mix, prazo e flexibilidade precisam atender à demanda. Há mismatch quando demanda incerta depende de lotes longos e inflexíveis.''')
S(a,T('Order qualifiers, winners og Forrestereffekten','Order qualifiers, winners and the bullwhip effect','Order qualifiers, winners e efeito chicote'),
'''Order qualifiers er minimumskrav for at komme i betragtning. Order winners er de forhold, som får kunden til at vælge virksomheden frem for en konkurrent. Et kriterium kan skifte rolle over tid og mellem kundetyper.
Forrestereffekten eller bullwhip-effekten betyder, at små udsving hos slutkunden kan blive større længere tilbage i kæden. Store partier, kampagner, forsinket information og skjulte sikkerhedsbestillinger kan forstærke den.
Del faktiske salg og lagre, planlæg kampagner sammen, reducer unødvendige partier og brug fælles prognoser. Procenterne på originalens slide er et forsøgs-eksempel, ikke en fast naturlov.
Opgaverne fra sidste slide er samlet i undersiden om egen virksomhed.''',
'''Order qualifiers are minimum requirements to be considered. Order winners cause customers to choose one supplier over another. Their role depends on customer segment, competition and time.
Forrestereffekten, or bullwhip effect, amplifies small customer-demand changes upstream. Large batches, promotions, delayed information and hidden precautionary orders can increase it.
Share actual sales/stock, jointly plan campaigns, reduce unnecessary batches and coordinate forecasts. The original slide’s percentages illustrate an experiment, not a fixed law.
The final slide’s tasks appear together on the own-company assignment page.''',
'''Order qualifiers são requisitos mínimos para ser considerado. Order winners fazem o cliente escolher uma empresa em vez de outra. O papel muda conforme segmento, concorrência e tempo.
Forrestereffekten, ou efeito chicote, amplia pequenas mudanças da demanda ao longo do upstream. Lotes grandes, promoções, informação atrasada e pedidos preventivos ocultos podem ampliá-lo.
Compartilhe vendas/estoques reais, planeje campanhas em conjunto, reduza lotes desnecessários e alinhe previsões. Os percentuais do slide ilustram um experimento, não uma regra fixa.
As tarefas do último slide estão reunidas na página da atividade sobre a própria empresa.''')

a=page(13,T('Artikel · fra just-in-time til just-in-case','Article · from just-in-time to just-in-case','Artigo · de just-in-time a just-in-case'),T('Kort resumé af den åbnede artikel. Linket er bevaret til videre læsning.','Brief summary of the retrieved article. The link is retained for further reading.','Resumo breve do artigo consultado. Link mantido para leitura adicional.'))
S(a,T('Forstå principperne','Understand the principles','Entenda os princípios'),
'''Just-in-time søger at få det nødvendige på det nødvendige tidspunkt og reducere unødigt lager. Just-in-case lægger større vægt på beredskab, fx bufferlager, alternative leverandører og kapacitetsmuligheder.
Studieopgave: Vælg en stabil standardvare og en kritisk vare med usikker forsyning. Hvilken buffer giver mening for hver? Hvilken fejl opstår, hvis du bruger samme strategi til begge? Forklar med leveringstid, efterspørgsel og mangelomkostninger.''',
'''Just-in-time aims to obtain what is needed when needed and reduce unnecessary stock. Just-in-case puts more emphasis on preparedness: buffers, alternative suppliers and capacity options.
Study task: choose a stable standard product and a critical product with uncertain supply. Which buffer suits each? What goes wrong if both use the same strategy? Use leveringstid, demand and mangelomkostninger in your explanation.''',
'''Just-in-time busca ter o necessário no momento necessário, reduzindo estoque desnecessário. Just-in-case dá mais peso à preparação: reservas, fornecedores alternativos e opções de capacidade.
Atividade: escolha um produto padrão estável e um crítico com fornecimento incerto. Qual reserva faz sentido em cada um? Qual erro surge ao usar a mesma estratégia? Explique usando leveringstid, demanda e mangelomkostninger.''','task')

a=page(14,T('Podcast · robusthed og AI','Podcast · resilience and AI','Podcast · resiliência e IA'),T('SCM Agendaen, 4. november 2025 · resumé af den ledsagende artikel, ikke af en fuld lydtransskription.','SCM Agendaen, 4 November 2025 · summary of the companion article, not a full audio transcript.','SCM Agendaen, 4 de novembro de 2025 · resumo do artigo associado, não de uma transcrição integral do áudio.'))
S(a,T('Resumé af artikelbeskrivelsen','Companion-article summary','Resumo do artigo associado'),
'''Podcastens artikel beskriver risikostyring på tværs af leverandørled. En fælles vurderingsmetode og scenarier skal gøre risiko synlig. Clearchain præsenterer AI-støttet dataindsamling og dashboards. Samtalen med Ole Overgaard og Michael Poulsen er sponsoreret af Clearchain; produktpåstande er ikke uafhængig dokumentation.''',
'''The companion article discusses risk management across supplier tiers, using shared assessment methods and scenarios. Clearchain presents AI-supported data collection and dashboards. The conversation with Ole Overgaard and Michael Poulsen is sponsored by Clearchain; product claims are not independent evidence.''',
'''O artigo associado aborda riscos nos vários níveis de fornecedores, com avaliação comum e cenários. A Clearchain apresenta coleta de dados apoiada por IA e painéis. A conversa com Ole Overgaard e Michael Poulsen é patrocinada pela Clearchain; alegações comerciais não são prova independente.''')
S(a,T('Øvelse med tre risici','Practice with three risks','Exercício com três riscos'),
'''- For hver risiko nedenfor: Hvad er årsagen, og hvad kan konsekvensen være?
- Hvordan vurderes sandsynlighed og konsekvens?
- Hvilke data er nødvendige, og hvem kontrollerer dem?
- Hvilken handling følger efter en alarm?
- Er påstanden generel faglig viden eller reklame for en løsning?
Øvelse: Beskriv en forsinket leverandør, en forkert lagerstatus og et IT-nedbrud. Foreslå ét forebyggende tiltag og én reaktion til hver. AI kan støtte overblik, men ukorrekte input giver ikke automatisk korrekte beslutninger.''',
'''- For each risk below, what is the cause and what could be the effect?
- How are probability and impact assessed?
- What data is needed and who checks it?
- What action follows an alert?
- Is a claim general knowledge or promotion of a solution?
Exercise: consider a delayed supplier, inaccurate stock data and an IT outage. Propose prevention and a response for each. AI may support visibility; wrong input does not automatically produce sound decisions.''',
'''- Para cada risco abaixo, qual é a causa e qual pode ser a consequência?
- Como avaliam probabilidade e impacto?
- Que dados são necessários e quem os verifica?
- Qual ação vem depois do alerta?
- É conhecimento geral ou publicidade de uma solução?
Exercício: considere fornecedor atrasado, estoque incorreto e queda de TI. Proponha uma prevenção e uma reação para cada. IA pode apoiar a visibilidade; entrada errada não gera automaticamente decisão correta.''','task')
a=page(15,T('Din virksomheds forsyningskæde','Your company’s supply chain','Cadeia de suprimentos da sua empresa'),T('De ti spørgsmål fra tekstfilen og den sidste SCM-slide er samlet her. Brug ét konkret produkt hele vejen.','The text file’s ten questions and final SCM slide are combined here. Use one specific product throughout.','As dez perguntas do TXT e do último slide de SCM estão reunidas aqui. Use um produto específico do início ao fim.'))
qs=[
T('1. Vurdér, hvordan I arbejder med SCM.','1. Assess how your business uses SCM.','1. Avalie como sua empresa trabalha com SCM.'),
T('2. Tegn virksomhedens logistiksystem.','2. Draw the company’s logistics system.','2. Desenhe o sistema logístico da empresa.'),
T('3. Vælg et af jeres stjerneprodukter.','3. Choose one of your star products.','3. Escolha um produto de destaque.'),
T('4. Tegn produktets forsyningskæde/netværk.','4. Draw its supply chain/network.','4. Desenhe a cadeia/rede desse produto.'),
T('5. Hvilke værdier og mål har aktørerne til fælles?','5. Which values and objectives do participants share?','5. Quais valores e objetivos os participantes compartilham?'),
T('6. Vælg 3–5 mulige udfordringer i kæden.','6. Identify 3–5 potential challenges.','6. Identifique de três a cinco desafios.'),
T('7. Vurdér jeres logistikstrategier.','7. Assess your logistics strategies.','7. Avalie as estratégias logísticas.'),
T('8. Giv eksempler på effektive og responsive forsyningskæder.','8. Give examples of efficient and responsive supply chains.','8. Dê exemplos de cadeias eficientes e responsivas.'),
T('9. Find eventuelle produkter med mismatch og forklar hvorfor.','9. Identify possible product/strategy mismatches and explain.','9. Identifique possíveis produtos em mismatch e explique.'),
T('10. Hvilke logistiske konkurrencefordele og forbedringsmuligheder har I?','10. Which logistics advantages and improvement opportunities exist?','10. Quais vantagens logísticas e oportunidades de melhoria existem?')]
for q in qs:S(a,q,T('Svar med et konkret eksempel og din begrundelse.','Answer with a concrete example and reasoning.','Responda com exemplo concreto e justificativa.')['da'], 'Answer with a concrete example and reasoning.','Responda com exemplo concreto e justificativa.','task')
S(a,T('Model · IKEA, tilpas til dit eget arbejde','Model · IKEA, adapt to your work','Modelo · IKEA, adapte ao seu trabalho'),
'''1. SCM kræver, at salg, lager, varehus og leverandørled deler behov og leveringsinformation. Beskriv de systemer og møder, du selv kender; gæt ikke navne.
2. Tegn varemodtagelse → lagerplacering → genopfyldning eller ordrepluk → udlevering/transport. Tilføj returflow og informationsflow begge veje.
3. Vælg fx en reol eller stol, som du faktisk håndterer. Notér artikelnummer, variant og kolli fra godkendte oplysninger.
4. Vis råmateriale → komponent/produktion → distribution → varehus eller kundelevering. Dette er en forenklet model; bekræft den konkrete rute.
5. Fælles mål kan være tilgængelighed, korrekt kvalitet, lav totalomkostning, sikkerhed og pålidelige data.
6. Mulige udfordringer: forsinkelse, skadet kolli, forkert beholdning, kampagneudsving og pladsmangel. Brug kun hændelser, du må dele.
7. Standardvarer med stabilt salg kan passe til en effektiv strategi. Usikre sæsonvarer kan kræve mere responsiv planlægning.
8. Sammenlign en stabil basisvare med en sæsonvare. Forklar behov for pris, buffer og leveringstid.
9. Mismatch kan være en kampagnevare med lang ufleksibel genbestilling eller en langsom vare med for stort sikkerhedslager. Det er en hypotese, indtil den understøttes af data.
10. Mulige fordele: tilgængelighed, nem afhentning og god information. Mulige forbedringer: mere præcis registrering, bedre prioritering og tidlig besked om afvigelser. Knyt hvert forslag til et mål og en måling.''',
'''1. SCM requires sales, warehouse, store and suppliers to share demand/delivery information. Describe systems and meetings you know; do not guess names.
2. Draw receiving → storage → replenishment or picking → collection/transport, with reverse goods and two-way information flows.
3. Choose a bookcase/chair you actually handle. Record article, variant and packages from approved information.
4. Show raw material → components/production → distribution → store or customer. Confirm the actual route; this is simplified.
5. Shared aims may include availability, quality, total cost, safety and reliable data.
6. Possible challenges: delays, damage, inaccurate stock, campaign peaks and space constraints. Share only permitted observations.
7. Stable standard products may suit an efficient strategy; uncertain seasonal items may need responsive planning.
8. Compare a basic product with a seasonal one using price, buffer and lead time.
9. Possible mismatch: a campaign item with long inflexible replenishment, or a slow mover with excessive safety stock. Treat as a hypothesis until supported by data.
10. Possible strengths: availability, easy collection and useful information. Improvements: accurate registration, prioritisation and early exception alerts. Link each to an objective and metric.''',
'''1. SCM exige compartilhar demanda e informação de entrega entre vendas, depósito, loja e fornecedores. Descreva os sistemas e reuniões que conhece; não adivinhe nomes.
2. Desenhe recebimento → localização → reposição ou separação → retirada/transporte, com retorno e informação nos dois sentidos.
3. Escolha estante/cadeira que realmente manuseia. Registre código, variante e volumes por fontes aprovadas.
4. Mostre matéria-prima → componentes/produção → distribuição → loja ou cliente. Confirme a rota real; é simplificação.
5. Objetivos comuns: disponibilidade, qualidade, custo total, segurança e dados confiáveis.
6. Desafios possíveis: atraso, avaria, estoque incorreto, pico de campanha e falta de espaço. Compartilhe apenas observações permitidas.
7. Itens padrão estáveis podem usar estratégia eficiente; sazonais incertos podem precisar de resposta flexível.
8. Compare um básico e um sazonal por preço, reserva e prazo.
9. Mismatch possível: produto de campanha com reposição longa/inflexível ou item lento com reserva excessiva. Trate como hipótese até ter dados.
10. Vantagens possíveis: disponibilidade, retirada fácil e boa informação. Melhorias: registros precisos, priorização e alerta antecipado. Relacione cada proposta a um objetivo e indicador.''','answer')

a=page(16,T('NordTrade · case og datagrundlag','NordTrade · case and data','NordTrade · caso e dados'),T('En fiktiv handelsvirksomhed. Brug tallene som fælles datagrundlag for ugeopgaven.','A fictional trading company. Use these figures as the common basis for the weekly assignment.','Empresa comercial fictícia. Use estes números como base comum do trabalho da semana.'))
S(a,T('Virksomhed, kunder og leverandører','Business, customers and suppliers','Empresa, clientes e fornecedores'),
'''NordTrade A/S har hovedkontor og centrallager i Kolding. Den sælger småmøbler, lamper, køkkenudstyr og boligtilbehør. Årlig omsætning ca. 220 mio. kr.; 65 ansatte.
Kunder: mindre/mellemstore detailbutikker, webshops i Danmark/Norge/Sverige og private via egen dansk webshop. Virksomheden importerer fra Europa/Asien og eksporterer til Norge/Sverige.
45 faste leverandører: 20 i EU, 15 i Asien og 10 danske/nordiske. Tre indkøbere bruger især de seneste 12 måneders salg og sigter mod lager til otte ugers salg. Asien leverer ofte hele containere; EU leverer typisk paller med kortere leveringstid.
Store indkøb reducerer enhedspris/fragt, men binder kapital. Populære varer kan samtidig blive udsolgt, hvis prognosen er forkert.''',
'''NordTrade has its head office and central warehouse in Kolding. It sells small furniture, lamps, kitchenware and home accessories. Annual revenue is about DKK 220m; 65 employees.
Customers include smaller/medium retailers, webshops in Denmark/Norway/Sweden and consumers through its Danish webshop. It imports from Europe/Asia and exports to Norway/Sweden.
It has 45 suppliers: 20 EU, 15 Asian and 10 Danish/Nordic. Three buyers mainly use the last 12 months’ sales, targeting eight weeks’ stock. Asian deliveries often use full containers; EU deliveries usually use pallets and shorter lead times.
Large purchases can reduce unit/freight cost but tie up capital. Popular products can still run out when forecasts are wrong.''',
'''NordTrade tem sede e depósito central em Kolding. Vende pequenos móveis, luminárias, utensílios e acessórios de casa. Faturamento anual de cerca de DKK 220 milhões; 65 funcionários.
Clientes: varejistas pequenos/médios, webshops na Dinamarca/Noruega/Suécia e consumidores pelo site dinamarquês. Importa de Europa/Ásia e exporta para Noruega/Suécia.
São 45 fornecedores: 20 UE, 15 Ásia e 10 dinamarqueses/nórdicos. Três compradores usam sobretudo os últimos 12 meses de vendas e miram oito semanas de estoque. Ásia geralmente manda contêineres completos; UE, paletes com prazo menor.
Compras grandes reduzem custo unitário/frete, mas prendem capital. Itens populares ainda podem faltar se a previsão estiver errada.''')
S(a,T('Varemodtagelse og lager','Receiving and warehousing','Recebimento e armazenagem'),
'''Lageret er 6.000 m² med ca. 3.500 SKU’er. Områder: modtagelse, pallereoler, pluklokationer, pakning og returzone. Personale: en lagerchef, otte på daghold og to studentermedhjælpere i eftermiddag/spidsbelastning.
Chaufføren melder ankomst, får port, og varerne kontrolleres mod følgeseddel og indkøbsordre. Afvigelser skrives i skema/Excel, varerne registreres i ERP og placeres. Kontrol er nogle gange for overfladisk i november–december, og fejl opdages først hos kunden.
Papirpluk er sorteret efter rute. FIFO ønskes, men følges ikke altid. Optælling foregår årligt i januar, med få løbende stikprøver. Det giver risiko for forsinkede beholdningsrettelser.
Svind er under ca. 0,8 % af lagerværdien. Gennemsnitlige lagerdage er steget fra 54 til 68 på to år. Kampagner og sæsonvarer giver pladsmangel.''',
'''The 6,000 m² warehouse holds about 3,500 SKUs. Zones: receiving, pallet racks, picking, packing and returns. Staff: one manager, eight day workers and two student assistants for afternoons/peaks.
The driver checks in and gets a dock; goods are checked against delivery note and purchase order. Exceptions go to a form/Excel, goods enter ERP and are stored. Peak-season checks in November–December can be superficial, leaving customers to discover errors.
Paper picking follows aisle routes. FIFO is intended but inconsistent. Stocktaking happens annually in January, with few cycle checks, delaying corrections.
Shrinkage stays below about 0.8% of inventory value. Average lagerdage rise from 54 to 68 in two years. Campaigns/seasonal goods strain space.''',
'''O depósito de 6.000 m² tem cerca de 3.500 SKUs. Áreas: recebimento, porta-paletes, separação, embalagem e devoluções. Equipe: um gerente, oito pessoas no dia e dois estudantes à tarde/nos picos.
Motorista anuncia chegada e recebe doca; mercadorias são conferidas contra nota e pedido de compra. Desvios vão para formulário/Excel; produtos entram no ERP e são localizados. Em novembro/dezembro a conferência pode ser superficial, deixando erros para o cliente descobrir.
Separação em papel segue a rota dos corredores. FIFO é pretendido, mas irregular. Há inventário anual em janeiro e poucas conferências contínuas, atrasando correções.
Perdas ficam abaixo de cerca de 0,8% do valor de estoque. Lagerdage médios sobem de 54 para 68 em dois anos. Campanhas/sazonais pressionam o espaço.''')
S(a,T('Salg, kundeservice og udgående flow','Sales, service and outbound flow','Vendas, atendimento e fluxo de saída'),
'''Salg: seks eksterne sælgere, fire i ordreafdelingen, B2B-portal og B2C-webshop. Tre kundeservicemedarbejdere håndterer reklamationer, levering, restordrer og produktspørgsmål.
Kundeordre → ERP → plukordre → pluk/pak/label → transportør → elektronisk faktura. Pluksedler udskrives kl. 8. En anden medarbejder kontrollerer i pakningen. Retur registreres på webshoppen; varen kontrolleres og genindlagres, hvis salgbar, og refunderes. Returårsager registreres kun begrænset.
87 % af kunderne er tilfredse/meget tilfredse med kundeservice. 90 % af mails besvares inden 24 timer. Henvendelser om restordrer/udsolgt er steget 25 % på et år. Nogle kunder modtager kun 80–90 % af ordren første gang.
250–350 ordrer afsendes dagligt: 70 % danske B2B, 20 % B2B Norge/Sverige, 10 % danske B2C. GLS bruges til små pakker/B2C; Danske Fragtmænd til danske paller; DHL til Norge/Sverige. Målet er 1–2 hverdage i DK og 3–5 i Norge/Sverige.''',
'''Sales: six field salespeople, four order staff, B2B portal and B2C webshop. Three customer-service staff handle claims, deliveries, backorders and product questions.
Order → ERP → picking order → pick/pack/label → carrier → electronic invoice. Pick lists print at 08:00. Another employee checks at packing. Web returns are inspected, restocked if saleable and refunded; return-cause statistics are limited.
Customer-service satisfaction is 87%; 90% of emails receive a reply within 24 hours. Backorder/out-of-stock queries rise 25% in a year. Some orders are initially only 80–90% complete.
Daily dispatches: 250–350 orders; 70% Danish B2B, 20% Norway/Sweden B2B, 10% Danish B2C. GLS handles small/B2C parcels, Danske Fragtmænd Danish pallets and DHL Norway/Sweden. Targets: 1–2 working days in Denmark, 3–5 in Norway/Sweden.''',
'''Vendas: seis representantes, quatro pessoas em pedidos, portal B2B e loja B2C. Três atendentes cuidam de reclamações, entrega, pendências e dúvidas.
Pedido → ERP → ordem de separação → separar/embalar/etiquetar → transportadora → fatura eletrônica. Listas saem às 8h. Outra pessoa confere na embalagem. Devoluções online são inspecionadas, recolocadas se vendáveis e reembolsadas; há pouca estatística das causas.
Satisfação do atendimento: 87%; 90% dos e-mails respondidos em 24 horas. Consultas de faltas/pendências sobem 25% no ano. Alguns pedidos chegam apenas 80–90% completos na primeira vez.
Expedição: 250–350 pedidos/dia; 70% B2B Dinamarca, 20% B2B Noruega/Suécia, 10% B2C Dinamarca. GLS: pacotes pequenos/B2C; Danske Fragtmænd: paletes nacionais; DHL: Noruega/Suécia. Metas: 1–2 dias úteis na Dinamarca, 3–5 na Noruega/Suécia.''')
S(a,T('Nøgletal · faktisk og mål','Metrics · actual and target','Indicadores · realizado e meta'),
'''Nøgletal | Faktisk | Mål / sammenligning
Omsætning | 220 mio. kr. | Datagrundlag 2024
Logistikomkostninger | 26,4 mio. kr. / 12 % | Højst 11 %
Leveringssikkerhed | 94 % | 97 %
Lagerservicegrad | 89 % af ordrelinjer straks fra lager | Intet eksplicit mål i casen
Gennemsnitlig DK-levering | 1,8 hverdage | 1–2 hverdage
Returprocent | 3,5 % af ordrelinjer | Intet eksplicit mål
Lagerdage | 68 | Tidligere 54
Transportomkostninger | +12 % på to år | Pres fra brændstof og dårligt fyldte paller
Bemærk enhederne: 89 % måles på ordrelinjer, mens 94 % beskriver korrekt og komplet levering til tiden. De må ikke bruges som samme måling.''',
'''Metric | Actual | Target / comparison
Revenue | DKK 220m | 2024 case data
Logistics costs (Logistikomkostninger) | DKK 26.4m / 12% | At most 11%
Delivery reliability (Leveringssikkerhed) | 94% | 97%
Immediate stock service (Lagerservicegrad) | 89% of lines immediately from stock | No explicit target
Average Danish delivery | 1.8 working days | 1–2 working days
Return rate | 3.5% of order lines | No explicit target
Inventory days (Lagerdage) | 68 | Previously 54
Transport costs (Transportomkostninger) | +12% in two years | Fuel and low pallet fill
The 89% measure uses order lines; 94% means correct, complete, on-time delivery. These are different metrics.''',
'''Indicador | Realizado | Meta / comparação
Faturamento | DKK 220 milhões | Dados de 2024 do caso
Custos logísticos (Logistikomkostninger) | DKK 26,4 milhões / 12% | Máximo 11%
Confiabilidade da entrega (Leveringssikkerhed) | 94% | 97%
Nível de atendimento imediato pelo estoque (Lagerservicegrad) | 89% das linhas atendidas imediatamente | Sem meta explícita
Entrega média Dinamarca | 1,8 dia útil | 1–2 dias úteis
Devolução | 3,5% das linhas | Sem meta explícita
Dias de estoque (Lagerdage) | 68 | Antes 54
Custos de transporte (Transportomkostninger) | +12% em dois anos | Combustível e paletes pouco cheios
Os 89% medem linhas; 94% significa entrega correta, completa e pontual. Não são o mesmo indicador.''')
S(a,T('SCM, konkurrence og procedurer','SCM, competition and procedures','SCM, concorrência e procedimentos'),
'''Tre store leverandører i Tyskland/Polen får månedlige salgsdata. To asiatiske leverandører accepterer rammeordrer med løbende træk. En stor dansk detailkæde koordinerer kampagner. Tysk samarbejde har reduceret restordrer på de berørte varer med 30 %, men meget data går manuelt i Excel/mail, og ikke alle vil dele prognoser.
NordTrade tilbyder hurtig levering, ekspres mod gebyr ved ordre før kl. 12, click & collect og returlabel til B2C. Konkurrenter tilbyder blandt andet samme dag, gratis fragt over en grænse og fleksible leveringsvinduer.
Indkøb gennemgår salg/lager månedligt. Under fire ugers forventet salg er kritisk; ordrebekræftelse kontrolleres manuelt, og pris/dato noteres i Excel. Modtagelsesrapport og afvigelser er ofte papirbaserede og registreres ikke altid straks i ERP.
Udfordringen er at forbedre service uden at øge totalomkostningen: færre fejl, mere præcise data, passende lager og bedre transportudnyttelse.''',
'''Three major German/Polish suppliers receive monthly sales data. Two Asian suppliers accept blanket orders with call-offs. A large Danish retailer coordinates campaigns. German cooperation cuts backorders on affected items by 30%, but much data still moves manually via Excel/email and not all suppliers share forecasts.
NordTrade offers fast delivery, paid express for orders before noon, click & collect and B2C return labels. Competitors offer same-day delivery, free freight thresholds and flexible windows.
Purchasing reviews sales/stock monthly. Below four weeks’ expected sales is critical; confirmations are manually checked and prices/dates entered in Excel. Receiving reports/exceptions often remain on paper and are not promptly reflected in ERP.
The challenge is better service without greater total costs: fewer errors, accurate data, suitable inventory and improved transport utilisation.''',
'''Três grandes fornecedores alemães/poloneses recebem vendas mensais. Dois asiáticos aceitam pedidos-quadro com retiradas graduais. Uma rede dinamarquesa coordena campanhas. A cooperação alemã reduz pendências dos itens envolvidos em 30%, mas dados ainda circulam manualmente em Excel/e-mail e nem todos compartilham previsões.
NordTrade oferece entrega rápida, expresso pago para pedido antes do meio-dia, click & collect e etiqueta de devolução B2C. Concorrentes oferecem entrega no dia, frete grátis acima de valor e janelas flexíveis.
Compras revisa vendas/estoque mensalmente. Menos de quatro semanas de venda esperada é crítico; confirmações são conferidas manualmente e preço/data vão ao Excel. Recebimento/desvios ficam frequentemente em papel e não entram imediatamente no ERP.
O desafio é melhorar serviço sem elevar custo total: menos erros, dados precisos, estoque adequado e transporte melhor aproveitado.''')
a=page(17,T('NordTrade · arbejdsspørgsmål og modeller','NordTrade · questions and models','NordTrade · perguntas e modelos'),T('Alle arbejder med samme case. Der er fire gruppefokus og fem dele. Brug begrundelser og angiv antagelser.','All groups use the same case: four focus areas and five parts. Explain your reasoning and assumptions.','Todos usam o mesmo caso: quatro focos de grupo e cinco partes. Justifique e declare premissas.'))
S(a,T('Grupper og arbejdsform','Groups and approach','Grupos e organização'),
'''Gruppe | Fokus
1 | Indgående logistik og lager.
2 | Lager og udgående logistik.
3 | SCM og leverandørsamarbejde.
4 | Salg, kundeservice og logistik som konkurrenceparameter.
Flere grupper kan have samme fokus. De fem dele er: konkrete oplysninger; succeser/udfordringer; dilemmaer; forbedringer; modeller/klassificeringer. Skeln mellem faktum fra casen og din egen vurdering.''',
'''Group | Focus
1 | Indgående logistik and lager.
2 | Lager and udgående logistik.
3 | SCM and supplier cooperation.
4 | Sales, customer service and logistics competition.
Multiple groups may share a focus. The five parts cover facts, successes/challenges, dilemmas, improvements and models/classifications. Separate case facts from your judgements.''',
'''Grupo | Foco
1 | Indgående logistik e lager.
2 | Lager e udgående logistik.
3 | SCM e colaboração com fornecedores.
4 | Vendas, atendimento e logística competitiva.
Mais de um grupo pode ter o mesmo foco. As cinco partes: fatos, sucessos/desafios, dilemas, melhorias e modelos/classificações. Separe fato do caso e avaliação sua.''')
S(a,T('Del 1 · find oplysningerne','Part 1 · find the facts','Parte 1 · encontre os dados'),
'''Alle: Find årlig omsætning, antal ansatte, SKU’er, placering af hovedkontor/lager, mindst tre kundetyper og leverandørfordeling. Find omkostningsmål/faktisk procent, leveringssikkerhed, lagerservicegrad, returprocent, lagerdage nu/før og leveringstider DK/Norge/Sverige.
Gruppe 1: Hvor ofte tælles lageret? Hvilken lagerrotation ønskes? Hvilke to modtagelsesenheder bruges typisk?
Gruppe 2: Hvor mange ordrer dagligt? Hvilke tre transportører? Faktisk og ønsket leveringssikkerhed?
Gruppe 3: Hvor mange leverandører? Mindst to SCM-tiltag? Hvor stor forbedring gav tysk samarbejde?
Gruppe 4: Kundetilfredshed? Mails besvaret inden 24 timer? Mindst tre markedsførte logistikservices?''',
'''Everyone: find annual revenue, employees, SKUs, office/warehouse location, at least three customer types and supplier distribution. Find logistics-cost target/actual, delivery reliability, stock service, return rate, current/previous stock days and Denmark/Norway/Sweden delivery targets.
Group 1: stocktaking frequency, intended rotation method and two typical inbound load units?
Group 2: daily orders, three carriers and actual/target delivery reliability?
Group 3: supplier count, at least two SCM initiatives and improvement from German cooperation?
Group 4: customer satisfaction, emails answered within 24 hours and at least three advertised logistics services?''',
'''Todos: encontre faturamento, funcionários, SKUs, sede/depósito, três tipos de cliente e distribuição dos fornecedores. Ache custo logístico meta/real, confiabilidade, atendimento do estoque, devoluções, dias de estoque antes/agora e prazos Dinamarca/Noruega/Suécia.
Grupo 1: frequência de inventário, método de rotação pretendido e duas unidades típicas recebidas?
Grupo 2: pedidos diários, três transportadoras e confiabilidade real/meta?
Grupo 3: total de fornecedores, dois exemplos de SCM e melhoria com parceiros alemães?
Grupo 4: satisfação, e-mails respondidos em 24 horas e três serviços logísticos divulgados?''','task')
S(a,T('Del 1 · svaroversigt','Part 1 · answer reference','Parte 1 · respostas de referência'),
'''Fælles: 220 mio. kr.; 65 ansatte; 3.500 SKU’er; Kolding. Kunder: detailbutikker, webshops og private. 45 leverandører: 20 EU, 15 Asien, 10 DK/Norden. Omkostninger 12 % mod højst 11 %. Leveringssikkerhed 94 %, mål 97 %. Lagerservicegrad 89 % af ordrelinjer. Retur 3,5 %. Lagerdage 68 mod tidligere 54. Leveringsmål: DK 1–2 hverdage; Norge/Sverige 3–5.
Gruppe 1: årlig januaroptælling; FIFO; containere fra Asien og paller fra EU.
Gruppe 2: 250–350 ordrer/dag; GLS, Danske Fragtmænd, DHL; 94 % mod 97 %.
Gruppe 3: 45; salgsdatadeling, rammeordrer med træk og fælles kampagner; 30 % færre restordrer på relevante tyske varer.
Gruppe 4: 87 % tilfredse/meget tilfredse; 90 % mails inden 24 timer; hurtig standardlevering, betalt ekspres, click & collect og nem retur.''',
'''Common: DKK 220m; 65 employees; 3,500 SKUs; Kolding. Customers: retailers, webshops, consumers. 45 suppliers: 20 EU, 15 Asia, 10 Danish/Nordic. Costs 12% versus max 11%. Reliability 94%, target 97%. Lagerservicegrad 89% of lines. Returns 3.5%. Stock days 68, previously 54. Delivery: Denmark 1–2 working days; Norway/Sweden 3–5.
Group 1: annual January stocktake; FIFO; Asian containers and EU pallets.
Group 2: 250–350 orders/day; GLS, Danske Fragtmænd, DHL; 94% versus 97%.
Group 3: 45 suppliers; sales sharing, blanket orders/call-offs and joint campaigns; 30% fewer backorders on affected German products.
Group 4: 87% satisfaction; 90% emails in 24 hours; fast standard delivery, paid express, click & collect and easy returns.''',
'''Comum: DKK 220 milhões; 65 funcionários; 3.500 SKUs; Kolding. Clientes: varejistas, webshops, consumidores. 45 fornecedores: 20 UE, 15 Ásia, 10 DK/nórdicos. Custos 12% versus máximo 11%. Confiabilidade 94%, meta 97%. Lagerservicegrad 89% das linhas. Devolução 3,5%. Estoque 68 dias, antes 54. Prazo: Dinamarca 1–2 dias úteis; Noruega/Suécia 3–5.
Grupo 1: inventário anual em janeiro; FIFO; contêineres asiáticos e paletes europeus.
Grupo 2: 250–350 pedidos/dia; GLS, Danske Fragtmænd, DHL; 94% versus 97%.
Grupo 3: 45 fornecedores; compartilhar vendas, pedidos-quadro e campanhas conjuntas; 30% menos pendências nos itens alemães envolvidos.
Grupo 4: satisfação 87%; 90% de e-mails em 24 horas; padrão rápido, expresso pago, click & collect e devolução fácil.''','answer')
S(a,T('Del 2 · succeser og udfordringer','Part 2 · successes and challenges','Parte 2 · sucessos e desafios'),
'''Alle: Find mindst tre succeser og tre udfordringer. Vurdér hvert logistikmål som stærkt, svagt eller midt imellem med belæg.
Gruppe 1: mindst to styrker ved modtagelse/lager og problemer med lagerdage, plads og optælling.
Gruppe 2: hvad fungerer ved pluk/pak/levering, og hvilke problemer giver restordrer og stigende fragt?
Gruppe 3: gevinster ved SCM og problemer ved manuel Excel/mail.
Gruppe 4: styrker ved kundeservice og udfordringer i konkurrencen på logistik.''',
'''Everyone: identify at least three successes and three challenges. Assess each logistics objective as strong, weak or intermediate with evidence.
Group 1: two receiving/warehouse strengths and issues with stock days, space and counting.
Group 2: strengths in pick/pack/delivery and problems from backorders/freight costs.
Group 3: SCM gains and problems with manual Excel/email.
Group 4: service strengths and logistics competition challenges.''',
'''Todos: identifique três sucessos e três desafios. Avalie cada objetivo como forte, fraco ou intermediário, com evidência.
Grupo 1: duas forças de recebimento/depósito e problemas de dias, espaço e inventário.
Grupo 2: pontos fortes de separação/embalagem/entrega e efeitos de faltas/frete.
Grupo 3: ganhos de SCM e problemas do Excel/e-mail manual.
Grupo 4: forças do atendimento e dificuldades competitivas da logística.''','task')
S(a,T('Del 2 · modelanalyse','Part 2 · model analysis','Parte 2 · análise-modelo'),
'''Succeser: lavt svind omkring 0,8 %, kundeservice 87 %, 90 % mailrespons og 30 % færre restordrer i et leverandørsamarbejde. Udfordringer: lagerdage +14, service 94 % under mål 97 %, omkostninger 12 % over mål 11 %, papirprocesser og pladsmangel.
Gruppe 1: fast modtagelsesflow og ERP-registrering er styrker; ujævn kontrol og årlig optælling gør fejl langvarige.
Gruppe 2: ruteordnet pluk og dobbeltkontrol er styrker; restordrer giver ekstra pluk/forsendelser og utilfredshed, mens lav fyldningsgrad øger pris pr. ordre.
Gruppe 3: fælles salg og rammeordrer hjælper; manuel dataudveksling giver versioner, forsinkelse og genindtastning.
Gruppe 4: hurtige svar og flere leveringsmuligheder er styrker; konkurrenters samme-dag og gratis fragt skaber forventninger, som NordTrade ikke bør love uden en økonomisk model.
En foreslået 1–5-vurdering af de syv mål findes i del 5. Karaktererne er vurderinger, ikke casefakta.''',
'''Successes: shrinkage around 0.8%, service satisfaction 87%, 90% email response and a 30% backorder reduction in a supplier partnership. Challenges: stock days +14, reliability 94% versus 97%, costs 12% versus 11%, paper processes and space constraints.
Group 1: structured receiving and ERP are strengths; inconsistent checks and annual counts prolong errors.
Group 2: route-based picking and a second check help; backorders create repeat work/shipments and dissatisfaction, while poor fill increases cost/order.
Group 3: shared sales and blanket orders help; manual data causes version conflicts, delays and re-entry.
Group 4: fast responses and delivery options help; competitor same-day/free shipping creates expectations requiring an economic model before promises.
Suggested 1–5 objective ratings appear in part 5. Ratings are judgements, not case facts.''',
'''Sucessos: perdas próximas de 0,8%, satisfação 87%, resposta de e-mail 90% e redução de pendências de 30% em parceria. Desafios: estoque +14 dias, confiabilidade 94% versus 97%, custos 12% versus 11%, papel e espaço.
Grupo 1: recebimento estruturado e ERP são forças; conferência irregular e inventário anual prolongam erros.
Grupo 2: rota de separação e dupla conferência ajudam; pendências geram retrabalho/fretes e insatisfação, enquanto baixa ocupação eleva custo por pedido.
Grupo 3: vendas compartilhadas e pedidos-quadro ajudam; trabalho manual cria versões, atrasos e redigitação.
Grupo 4: resposta rápida e opções ajudam; concorrentes com entrega no dia/frete grátis elevam expectativas que exigem análise econômica antes da promessa.
As notas sugeridas de 1–5 estão na parte 5. São julgamentos, não fatos do caso.''','answer')
S(a,T('Del 3 · dilemmaer','Part 3 · dilemmas','Parte 3 · dilemas'),
'''Alle: 1. Lavere lagerbinding eller højere leveringssikkerhed? 2. Billigere samlet transport eller hurtigst mulig levering? 3. Samme service til alle eller differentierede niveauer? Vælg og begrund med både omkostning og kundevirkning.
Gruppe 1: store billige indkøb fra Asien eller mindre hyppige partier?
Gruppe 2: investér i digital pluk/scannere eller fortsæt med papir?
Gruppe 3: kræv mere datadeling af alle med risiko for leverandørtab, eller samarbejd tæt med få?
Gruppe 4: gratis fragt over en grænse for at matche konkurrenter trods højere omkostning? Argumentér for og imod.''',
'''Everyone: 1. Lower lagerbinding or higher leveringssikkerhed? 2. Cheapest consolidated transport or fastest delivery? 3. Uniform or differentiated service? Choose and justify costs and customer effects.
Group 1: large cheap Asian purchases or smaller frequent batches?
Group 2: invest in scanners/digital picking or retain paper?
Group 3: require data sharing from all, risking supplier loss, or work deeply with a few?
Group 4: offer a free-shipping threshold despite higher costs? Discuss both sides.''',
'''Todos: 1. Menos lagerbinding ou mais leveringssikkerhed? 2. Transporte consolidado barato ou máximo de rapidez? 3. Serviço igual ou diferenciado? Escolha justificando custo e efeito ao cliente.
Grupo 1: grandes compras baratas da Ásia ou lotes menores frequentes?
Grupo 2: investir em scanners/separação digital ou manter papel?
Grupo 3: exigir dados de todos, arriscando perder fornecedores, ou colaborar com poucos?
Grupo 4: frete grátis acima de valor, apesar do custo maior? Argumente a favor e contra.''','task')
S(a,T('Del 3 · en begrundet balance','Part 3 · a reasoned balance','Parte 3 · equilíbrio justificado'),
'''1. Reducér lager selektivt: beskyt populære og kritiske varer, afvikl langsomme varer. Et generelt lagercut kan forværre de 89 %.
2. Brug planlagt standardtransport og betalt ekspres. Konsolidér uden at bryde de lovede 1–2 eller 3–5 dage.
3. Differentier efter behov og cost-to-serve med tydelige vilkår. Risikoen er kompleksitet og oplevet uretfærdighed; undgå ubegrundede særregler.
Gruppe 1: segmentér varer, brug rammeordrer og hyppigere træk, når lagerbesparelsen overstiger merfragt og indkøbspris.
Gruppe 2: pilotér scanning på et område. Sammenlign investering, oplæring, tid pr. linje og fejl før/efter. Gevinsten er mulig, ikke dokumenteret på forhånd.
Gruppe 3: fælles minimumskrav til alle, tæt forecast-samarbejde med strategiske partnere. Undgå unødig udskiftning af gode leverandører.
Gruppe 4: gratis fragt kan løfte kurven og konkurrencedygtigheden, men kan øge tab på små/lave-margin-ordrer. Beregn dækningsbidrag efter fragt, returer og service, før en grænse vælges.''',
'''1. Cut stock selectively: protect popular/critical items and clear slow movers. A blanket cut may worsen the 89%.
2. Use planned standard transport plus paid express. Consolidate within promised 1–2 or 3–5 days.
3. Differentiate by need and cost-to-serve with clear terms. Risks: complexity and perceived unfairness; avoid arbitrary exceptions.
Group 1: segment items and use blanket orders/call-offs when stock savings exceed extra freight/purchase cost.
Group 2: pilot scanning. Compare investment/training, time per line and error rates before/after. Benefits are possible, not proven in advance.
Group 3: common minimum data requirements with deeper forecasting for strategic partners; avoid unnecessarily losing good suppliers.
Group 4: free shipping may improve baskets/competitiveness but make small low-margin orders unprofitable. Calculate contribution after freight, returns and service before setting a threshold.''',
'''1. Reduza seletivamente: proteja populares/críticos e diminua lentos. Corte geral pode piorar os 89%.
2. Use padrão planejado e expresso pago. Consolide dentro dos 1–2 ou 3–5 dias prometidos.
3. Diferencie por necessidade e custo de atender, com regras claras. Riscos: complexidade e percepção de injustiça; evite exceções arbitrárias.
Grupo 1: segmente e use pedidos-quadro/retiradas quando economia de estoque superar frete/preço adicionais.
Grupo 2: pilote scanning. Compare investimento/treinamento, tempo por linha e erros antes/depois. Benefícios são possíveis, não comprovados previamente.
Grupo 3: requisitos mínimos de dados para todos e previsão conjunta com estratégicos; evite perder bons parceiros sem necessidade.
Grupo 4: frete grátis pode elevar cesta/competitividade, mas tornar pedidos pequenos de baixa margem deficitários. Calcule contribuição após frete, devoluções e serviço antes de definir limite.''','answer')
S(a,T('Del 4 · forbedringsplan','Part 4 · improvement plan','Parte 4 · plano de melhorias'),
'''Find mindst tre konkrete forslag: mindst ét om omkostninger og ét om service. Angiv handling, omkostningseffekt og kundeeffekt. Vurdér bidrag til 11 % og 97 % uden at love udokumenterede besparelser.
Gruppe 1: modtagelse, løbende optælling, lagerdage og ukurans.
Gruppe 2: pluk/pak, plads, pallefyld og transportaftaler.
Gruppe 3: dataudveksling, rammeordrer/VMI og fælles forecast/kampagner.
Gruppe 4: serviceniveauer, leveringskommunikation og markedsføring af logistiske løfter.''',
'''Propose at least three actions: at least one cost action and one service action. State implementation, cost and customer effects. Assess contribution to 11% costs and 97% reliability without inventing savings.
Group 1: receiving, cycle counts, stock days and obsolete items.
Group 2: pick/pack, space, pallet fill and carrier agreements.
Group 3: data exchange, blanket orders/VMI and shared forecasts/campaigns.
Group 4: service levels, delivery communication and logistics promises in marketing.''',
'''Proponha três ações: ao menos uma de custo e uma de serviço. Descreva execução, efeito no custo e no cliente. Avalie contribuição às metas 11% e 97% sem inventar economia.
Grupo 1: recebimento, contagem contínua, dias e obsolescência.
Grupo 2: separação/embalagem, espaço, ocupação de paletes e transportadoras.
Grupo 3: dados, pedidos-quadro/VMI e previsões/campanhas conjuntas.
Grupo 4: níveis de serviço, comunicação de prazos e promessas no marketing.''','task')
S(a,T('Del 4 · handling, effekt og måling','Part 4 · action, effect and measurement','Parte 4 · ação, efeito e medição'),
'''Forslag | Omkostning / service | Måling
Scanning ved modtagelse/pluk og straksregistrering | Investering først; færre fejl og bedre beholdning | Fejl pr. ordrelinje og lagerdifferencer.
ABC og løbende optælling | Arbejdstid til kontrol; færre mangler/ukurans | Service på A-varer, lagerdage og svind.
Pallekonsolidering og faste afgange | Lavere fragt pr. enhed; mulig ventetid | Fyldningsgrad, pris pr. ordre og rettidighed.
Fælles forecast og rammeordrer | Mindre buffer/hastearbejde; kræver integration | Restordrer, leverandørpræcision og datakvalitet.
Tydelig lager-/leveringsinformation og servicetrin | Færre henvendelser og realistiske løfter | Kontaktårsager og leveringssikkerhed.
11 % af 220 mio. = 24,2 mio. kr. mod 26,4 mio.: forskel 2,2 mio. kr., hvis omsætningen er uændret. Det svarer til 8,33 % af de nuværende logistikomkostninger.
Service fra 94 % til 97 % er +3 procentpoint. Fejlandelen går fra 6 % til 3 %: en halvering. En implementeringsplan skal dokumentere effekten, ikke blot påstå at den når målene.''',
'''Action | Cost / service effect | Measure
Receive/pick scanning and immediate updates | Upfront investment; fewer errors and accurate stock | Errors per line and stock discrepancies.
ABC plus cycle counting | Checking effort; fewer shortages/obsolete goods | A-item service, stock days and shrinkage.
Pallet consolidation and planned departures | Lower freight/unit; possible waiting | Fill rate, cost/order and punctuality.
Joint forecasts and blanket orders | Less buffering/expediting; integration needed | Backorders, supplier accuracy and data quality.
Clear availability/delivery data and service tiers | Fewer queries, realistic promises | Contact causes and reliability.
11% of DKK 220m = 24.2m versus 26.4m: a DKK 2.2m gap at unchanged revenue, or 8.33% of current logistics costs.
94% to 97% is +3 percentage points. Failures fall from 6% to 3%, a halving. Measure the plan’s impact rather than asserting it achieves both targets.''',
'''Ação | Efeito em custo / serviço | Indicador
Scanning e registro imediato | Investimento inicial; menos erros e estoque preciso | Erros por linha e diferenças de estoque.
ABC e contagem contínua | Tempo de controle; menos faltas/obsolescência | Serviço dos A, dias e perdas.
Consolidar paletes e planejar saídas | Frete menor/unidade; possível espera | Ocupação, custo/pedido e pontualidade.
Previsão conjunta e pedidos-quadro | Menos reservas/urgências; exige integração | Pendências, precisão e dados.
Disponibilidade/prazos claros e níveis de serviço | Menos contatos, promessas viáveis | Motivos dos contatos e confiabilidade.
11% de DKK 220 milhões = 24,2 milhões versus 26,4: diferença de 2,2 milhões, com faturamento constante. Equivale a 8,33% do custo logístico atual.
94% para 97% são +3 pontos percentuais. Falhas caem de 6% para 3%, pela metade. Meça o efeito do plano em vez de afirmar que ele garante as duas metas.''','answer')
S(a,T('Del 5 · modeller og klassificering','Part 5 · models and classifications','Parte 5 · modelos e classificações'),
'''Alle: tegn NordTrades værdikæde med indgående, lager/intern håndtering, udgående og salg/kundeservice. Skriv 1–2 opgaver, én succes og én udfordring pr. led. Lav et skema over de syv mål med beskrivelse, karakter 1–5 og én forbedring.
Gruppe 1: Lav ABC-model efter høj/mellem/lav omsætning og forskellig styring. Skriv modtagelsesprocedure i 1–8 trin med kontrolpunkter.
Gruppe 2: Tegn ordreflow fra bestilling til levering, markér fejl og ventetid. Klassificér efter størrelse og B2B/B2C og tilpas håndteringen.
Gruppe 3: Vis kæden og markér eksisterende/muligt SCM-samarbejde. Klassificér leverandører som strategiske, vigtige og standard med tilpassede krav.
Gruppe 4: Sammenlign pris, kvalitet, sortiment, service og logistik med en typisk konkurrent, karakter 1–5. Vælg differentiering. Skitsér basis/standard/premium med leveringstid, fragtpris, retur og målgruppe.''',
'''Everyone: draw NordTrade’s chain with inbound, warehouse/internal handling, outbound and sales/service. For each, add 1–2 tasks, one success and one challenge. Rate seven objectives 1–5 with evidence and one improvement.
Group 1: create high/medium/low-sales ABC categories with different control. Write a receiving procedure in 1–8 steps with checkpoints.
Group 2: draw order-to-delivery flow, marking errors/waits. Classify by size and B2B/B2C and adapt handling.
Group 3: map existing/potential SCM links. Classify strategic, important and standard suppliers with appropriate requirements.
Group 4: compare price, quality, assortment, service and logistics with a typical competitor, scoring 1–5. Choose differentiation. Design basic/standard/premium tiers with time, freight, returns and target groups.''',
'''Todos: desenhe entrada, depósito/manuseio, saída e vendas/atendimento. Para cada etapa, inclua 1–2 tarefas, um sucesso e um desafio. Dê notas 1–5 aos sete objetivos com evidência e melhoria.
Grupo 1: ABC por vendas altas/médias/baixas e controles distintos. Procedimento de recebimento em 1–8 passos com conferências.
Grupo 2: fluxo do pedido à entrega, marcando erros/esperas. Classifique por tamanho e B2B/B2C e adapte o manuseio.
Grupo 3: mapeie vínculos SCM existentes/possíveis. Classifique fornecedores estratégicos, importantes e padrão com requisitos adequados.
Grupo 4: compare preço, qualidade, sortimento, serviço e logística com concorrente típico, notas 1–5. Escolha diferenciação. Proponha básico/padrão/premium com prazo, frete, devolução e público.''','task')
S(a,T('Del 5 · værdikæde og syv mål','Part 5 · value chain and objectives','Parte 5 · cadeia e objetivos'),
'''Led | Opgaver | Succes | Udfordring
Indgående | Bestille, modtage og kontrollere | Faste leverandører og SCM | Overfladisk kontrol i spidsperioder
Lager | Placere, tælle og plukke | Lavt svind | 68 lagerdage, papir og plads
Udgående | Pakke, booke og levere | 94 % sikkerhed | Under mål og dyrere transport
Salg/service | Ordre, information og retur | 87 % tilfredshed | Flere restordrehenvendelser
Mål | Forslag til karakter | Begrundelse og forbedring
Rette produkt | 3 | Bredt sortiment, men langsomme varer: ryd op i sortimentet.
Rette mængde | 2 | Overlager samtidig med mangel: ABC og bedre forecast.
Rette kvalitet | 3 | Generelt god, enkelte fejl: målrettet modtagekontrol.
Rette sted | 3 | Kolding fungerer i DK, længere eksport: undersøg ruter, ikke automatisk nyt lager.
Rette tid | 3 | 94 % mod 97 %: realistiske løfter og flaskehalsstyring.
Rette kunde | 2 | Ukendt cost-to-serve: segmentér lønsomhed og behov.
Rette omkostning | 2 | 12 % mod 11 %: færre fejl og bedre fyldning.
Hvis opgaven bruger rette information, vurder manuel data og kundeløfter særskilt. Karakterer er et argumenteret forslag, ikke facit.''',
'''Stage | Tasks | Success | Challenge
Inbound | Purchase, receive, inspect | Established suppliers/SCM | Superficial peak checks
Warehouse | Store, count, pick | Low shrinkage | 68 stock days, paper, space
Outbound | Pack, book, deliver | 94% reliability | Below target, rising freight
Sales/service | Orders, information, returns | 87% satisfaction | More backorder queries
Objective | Suggested score | Evidence and improvement
Rette produkt | 3 | Broad assortment, slow movers: review assortment.
Rette mængde | 2 | Excess and shortages: ABC and forecasts.
Rette kvalitet | 3 | Generally good, some issues: targeted checks.
Rette sted | 3 | Kolding suits Denmark, slower exports: investigate routes before a new warehouse.
Rette tid | 3 | 94% versus 97%: realistic promises/bottleneck control.
Rette kunde | 2 | Unknown cost-to-serve: segment profit/needs.
Rette omkostning | 2 | 12% versus 11%: fewer errors/better fill.
If the task uses rette information, assess manual data/promises separately. Scores are reasoned examples, not fixed answers.''',
'''Etapa | Tarefas | Sucesso | Desafio
Entrada | Comprar, receber, conferir | Fornecedores/SCM estáveis | Controle superficial nos picos
Depósito | Localizar, contar, separar | Poucas perdas | 68 dias, papel, espaço
Saída | Embalar, reservar, entregar | Confiabilidade 94% | Abaixo da meta, frete subindo
Vendas/serviço | Pedido, informação, retorno | Satisfação 87% | Mais consultas de pendências
Objetivo | Nota sugerida | Evidência e melhoria
Rette produkt | 3 | Mix amplo e itens lentos: revisar sortimento.
Rette mængde | 2 | Excesso e falta: ABC/previsão.
Rette kvalitet | 3 | Geralmente boa, alguns problemas: conferência dirigida.
Rette sted | 3 | Kolding atende DK, exportação lenta: investigar rotas antes de novo depósito.
Rette tid | 3 | 94% versus 97%: promessas viáveis/gargalos.
Rette kunde | 2 | Custo de atender desconhecido: segmentar lucro/necessidade.
Rette omkostning | 2 | 12% versus 11%: menos erros/mais ocupação.
Se a tarefa usar rette information, avalie dados manuais/promessas separadamente. Notas são propostas justificadas, não gabarito fixo.''','answer')
S(a,T('Del 5 · fire gruppemodeller','Part 5 · four group models','Parte 5 · quatro modelos de grupo'),
'''Gruppe 1: Rangér varer efter årlig omsætningsværdi og vælg ABC-grænser ud fra data; der findes ingen SKU-tal i casen til en rigtig fordeling. A: tæt opfølgning og hyppig tælling. B: normal opfølgning. C: enklere kontrol og vurdering af langsomme varer. Høj omsætning er ikke nødvendigvis højt dækningsbidrag.
Modtagelse i otte trin: (1) ankomst/port; (2) match ordre og følgeseddel; (3) tæl kolli; (4) kontrollér artikel/variant; (5) se efter skader; (6) registrér afvigelse og adskil fejlvarer; (7) opdatér ERP straks; (8) placér/scann lokation og kontrollér afslutning.
Gruppe 2: Kundeordre → validering/ERP → lagerreservation → pluk → kontrol/pak → transport → levering. Fejl kan opstå ved indtastning, forkert beholdning, pluk og label. Ventetid opstår ved mangler, daglig kl. 8-udskrift og transportafgang. Små B2C-pakker kan standardiseres; store B2B-ordrer kan palleplanlægges; hasteordrer får tydelig betalt service.
Gruppe 3: EU/Asien/Norden → NordTrade → butikker/webshops/private. Markér månedlige salgsdata, rammeordrer og fælles kampagner som eksisterende. Foreslå automatisk EDI/API og afvigelsesvarsler. Strategiske: fælles forecast og beredskab; vigtige: KPI’er og regelmæssig opfølgning; standard: standardvilkår og enklere integration. Klassificér med betydning og risiko, ikke kun land.
Gruppe 4: Priser for en faktisk konkurrent mangler. En eksempelmatrix kan bruge NordTrade/typisk konkurrent: pris 3/3, kvalitet 3/3, sortiment 4/3, service 4/3, logistik 3/4. Det er illustrative antagelser, ikke undersøgte fakta. Vælg pålidelighed og gennemsigtighed som ønsket differentiering.
Servicepakke, forslag: basis med konsolideret levering og tydelig pris; standard med de lovede normale frister og tracking; premium med aftalt ekspres og højere gebyr. Returvilkår skal beskrives for hver målgruppe og bekræftes; opfind ikke aktuelle juridiske rettigheder eller gratis ydelser.''',
'''Group 1: rank products by annual sales value and choose ABC cut-offs from data; the case lacks SKU-level data for a real allocation. A: close monitoring/frequent counts; B: normal review; C: simpler control and slow-mover review. High sales do not necessarily mean high contribution.
Eight receiving steps: (1) arrival/dock; (2) match order/note; (3) count packages; (4) check article/variant; (5) inspect damage; (6) record exceptions/isolate faults; (7) update ERP immediately; (8) put away/scan location and verify completion.
Group 2: order → validation/ERP → reservation → picking → check/pack → transport → delivery. Errors: entry, stock, picking, labels. Waiting: shortages, 08:00 batch print, departure. Standardise small B2C parcels, pallet-plan large B2B and price urgent service clearly.
Group 3: EU/Asia/Nordics → NordTrade → retailers/webshops/consumers. Mark sales sharing, blanket orders and campaign planning as existing. Propose EDI/API and exception alerts. Strategic suppliers: shared forecasts/contingency; important: KPIs/reviews; standard: standard terms/simple integration. Use importance/risk, not country alone.
Group 4: real competitor figures are missing. An illustrative NordTrade/competitor matrix might score price 3/3, quality 3/3, assortment 4/3, service 4/3, logistics 3/4. These are assumptions, not researched facts. Choose reliability/transparency as intended differentiation.
Proposed tiers: basic consolidated delivery/clear charge; standard promised normal deadlines/tracking; premium agreed express at higher charge. Define and confirm returns for each segment; do not invent legal rights or free services.''',
'''Grupo 1: ordene itens por valor anual de vendas e escolha cortes ABC com dados; faltam dados por SKU para distribuição real. A: acompanhamento/conferência frequentes; B: normal; C: controle simples e revisão dos lentos. Vendas altas não significam contribuição alta.
Oito passos de recebimento: (1) chegada/doca; (2) cruzar pedido/nota; (3) contar volumes; (4) conferir código/variante; (5) inspecionar avaria; (6) registrar desvio/isolar erro; (7) atualizar ERP imediatamente; (8) localizar/escanear endereço e concluir conferência.
Grupo 2: pedido → validação/ERP → reserva → separação → conferir/embalar → transporte → entrega. Erros: digitação, estoque, separação e etiquetas. Espera: falta, impressão às 8h e saída. Padronize pequenos B2C, planeje paletes B2B grandes e precifique urgência claramente.
Grupo 3: UE/Ásia/Nórdicos → NordTrade → lojas/webshops/consumidores. Marque dados de vendas, pedidos-quadro e campanhas como existentes. Proponha EDI/API e alertas. Estratégicos: previsão/contingência conjunta; importantes: KPIs/revisões; padrão: termos comuns/integração simples. Use importância/risco, não só país.
Grupo 4: faltam números reais do concorrente. Matriz ilustrativa NordTrade/concorrente: preço 3/3, qualidade 3/3, sortimento 4/3, serviço 4/3, logística 3/4. São premissas, não pesquisa. Escolha confiabilidade/transparência como diferenciação desejada.
Pacotes propostos: básico consolidado/preço claro; padrão nos prazos normais/rastreamento; premium expresso acordado/taxa maior. Defina e confirme devoluções por segmento; não invente direitos legais nem gratuidades.''','answer')

a=page(18,T('Fremlæggelse og evaluering','Presentation and evaluation','Apresentação e avaliação'),T('Skeln mellem faglig fremlæggelse, trivsel, undervisningsmiljø og evaluering af forløbet.','Distinguish presentation, wellbeing, learning environment and course evaluation.','Distinga apresentação, bem-estar, ambiente de ensino e avaliação do curso.'))
S(a,T('Tre evalueringer i materialet','Three evaluations in the material','Três avaliações no material'),
'''Elevtrivsel: materialet siger hvert år i november. Gå til eud-trivsel.dk og brug Uni-login. Vælg kode frem for hold efter lærerens aktuelle instruktion.
Undervisningsmiljø: materialet siger generelt hvert andet år og henviser til 2025. Spørgsmål om forløb og uddannelse skal besvares efter dit rigtige forløb. Sliden nævner Kontor, handel og forretningsservice eller Fødevarer, handel og forretningsservice.
Undervisningsevaluering: ved afslutning af forløb. Sliden nævner Fødevarer/Business og en begrænset målgruppe. Bekræft med læreren, hvad der gælder for IKEA-holdet.
Originalen indeholder gamle QR-koder og kode zkX74S. Brug den kun, hvis læreren bekræfter, at den stadig gælder. Husk afslut-knappen. Vi har ikke udfyldt eller indsendt en evaluering.''',
'''Elevtrivsel: the material says annually in November. Visit eud-trivsel.dk and use Uni-login. Choose a code rather than a class according to current teacher instructions.
Learning environment: described as generally every two years, with a 2025 reference. Answer course/programme questions using your actual programme. Slides mention Kontor, handel og forretningsservice or Fødevarer, handel og forretningsservice.
Course evaluation: at the end of a course. Slides mention Fødevarer/Business and a limited target group. Confirm what applies to the IKEA class.
The original contains old QR codes and code zkX74S. Use only if the teacher confirms validity. Remember the finish button. No evaluation has been submitted.''',
'''Elevtrivsel: o material diz anualmente em novembro. Acesse eud-trivsel.dk e use Uni-login. Escolha código em vez de turma conforme a instrução atual do professor.
Ambiente de ensino: descrito como geralmente a cada dois anos, com referência a 2025. Informe seu curso real. Slides citam Kontor, handel og forretningsservice ou Fødevarer, handel og forretningsservice.
Avaliação do ensino: no final do período. Slides citam Fødevarer/Business e público específico. Confirme o que vale para a turma IKEA.
O original tem QR codes antigos e código zkX74S. Use somente se o professor confirmar validade. Lembre de concluir. Nenhuma avaliação foi enviada.''')
S(a,T('Forbered en kort fremlæggelse','Prepare a short presentation','Prepare uma apresentação curta'),
'''1. Præsentér virksomheden og jeres gruppefokus.
2. Vis tre vigtige fakta med enheder.
3. Forklar ét problem og dets årsag.
4. Vis et konkret forbedringsforslag og en mulig ulempe.
5. Afslut med, hvordan I vil måle effekten.
Øv sætningerne: Vores vigtigste udfordring er … Vi foreslår … Det kan reducere … En risiko er … Vi vil måle …''',
'''1. Introduce the business and group focus.
2. Show three important facts with units.
3. Explain one problem and its cause.
4. Present an improvement and possible drawback.
5. Explain how to measure the effect.
Practise Danish starters: Vores vigtigste udfordring er … Vi foreslår … Det kan reducere … En risiko er … Vi vil måle …''',
'''1. Apresente empresa e foco do grupo.
2. Mostre três fatos com unidades.
3. Explique um problema e a causa.
4. Proponha uma melhoria e uma possível desvantagem.
5. Explique como medir o efeito.
Treine os inícios em dinamarquês: Vores vigtigste udfordring er … Vi foreslår … Det kan reducere … En risiko er … Vi vil måle …''','task')

a=page(19,T('Samtaleskema · IKEA','Conversation form · IKEA','Formulário de conversa · IKEA'),T('Forbered ærlige eksempler til samtalen med læreren og din uddannelsesansvarlige.','Prepare honest examples for the conversation with your teacher and training supervisor.','Prepare exemplos honestos para conversar com o professor e a responsável pela formação.'))
S(a,T('Formål og efterfølgende brug','Purpose and follow-up','Objetivo e acompanhamento'),
'''Skemaet er udgangspunkt for samtalen mellem dig og lærerne. Lærernes vurdering gives under samtalen. Det færdige skema uploades ifølge materialet til uddataplus.dk og bruges i den efterfølgende samtale i varehuset.
Elevens selvevaluering og lærerteamets vurdering er to forskellige dele. Skriv ikke vurderinger på lærerens vegne. Svar ærligt og konkret; dette er ikke en opgave med ét korrekt facit.''',
'''The form supports a conversation between you and the teachers. Teachers provide their assessment during it. The completed form is uploaded to uddataplus.dk according to the material and used for follow-up at the store.
Self-assessment and the teaching team’s assessment are separate. Do not fill in the teacher’s judgement on their behalf. Be honest and concrete; there is no single correct answer.''',
'''O formulário orienta a conversa com os professores. A avaliação deles é dada durante a conversa. Segundo o material, o formulário concluído vai ao uddataplus.dk e apoia o acompanhamento na loja.
Autoavaliação e avaliação docente são partes distintas. Não preencha a avaliação do professor por ele. Seja honesta e concreta; não existe um único gabarito.''')
S(a,T('Alle spørgsmål til din forberedelse','All preparation questions','Todas as perguntas para preparar'),
'''Virksomheden: Hvordan går det? Hvilken afdeling arbejder du i? Hvilke ansvarsområder har du? Hvad går godt og mindre godt?
Forberedelse: Har du talt med din elev-/uddannelsesansvarlige? Hvordan forberedte du opgaver og præsentationer? Er der andet?
Skoleopholdet: Hvordan går det socialt i og uden for klassen? Er fagligt indhold let, passende, svært eller udfordrende? Hvordan går gruppe- og individuelt arbejde? Hvordan går det personligt?
Generelt: Hvilke udviklingsområder og fokuspunkter har du? Er der andet, du vil tale om?
Vurdér deltagelse, fagligt niveau og samarbejde som under middel, middel eller over middel, med kommentar.
Lærerteamet vurderer deltagelse, niveau, samarbejde, udvikling og fokus til kommende moduler. Der noteres også samtalens underviser.''',
'''Workplace: how is it going? Which department? Responsibilities? What goes well or less well?
Preparation: did you meet your training supervisor? How did you prepare assignments/presentations? Anything else?
School period: social life inside/outside class? Is content easy, appropriate, difficult or challenging? Group/individual work? Personal wellbeing?
General: development areas and priorities? Anything else you want to discuss?
Rate participation, professional level and cooperation below average, average or above average, with comments.
Teachers assess participation, level, cooperation, development and future-module priorities, and record the teacher conducting the conversation.''',
'''Empresa: como está indo? Qual departamento? Responsabilidades? O que vai bem ou menos bem?
Preparação: conversou com a responsável pela formação? Como preparou tarefas/apresentações? Mais algo?
Período escolar: convivência dentro/fora da turma? Conteúdo fácil, adequado, difícil ou desafiador? Trabalho em grupo/individual? Bem-estar pessoal?
Geral: áreas de desenvolvimento e prioridades? Outro assunto a conversar?
Avalie participação, nível técnico e colaboração como abaixo da média, média ou acima, comentando.
Professores avaliam participação, nível, colaboração, desenvolvimento e foco para próximos módulos, registrando quem conduziu a conversa.''','task')
S(a,T('Sproglig støtte · tilpas sandfærdigt','Language support · adapt truthfully','Apoio de linguagem · adapte com sinceridade'),
'''Jeg arbejder som logistikelev i IKEA. Mine opgaver er …
Det går godt med … Et konkret eksempel er …
Jeg synes, at de faglige begreber er udfordrende. Jeg vil gerne øve dem med eksempler fra lageret.
Jeg har forberedt mig ved at … Jeg har brug for hjælp til …
I gruppearbejdet bidrager jeg med … Mit næste mål er …
Udskift prikkerne med dine egne oplevelser. Vælg en lille handling: lær fem begreber, stil ét afklarende spørgsmål pr. undervisningsdag eller øv en kort forklaring med en kollega.''',
'''Danish sentence starters: Jeg arbejder som logistikelev i IKEA. Mine opgaver er … Det går godt med … Et konkret eksempel er …
To explain learning needs: Jeg synes, at de faglige begreber er udfordrende. Jeg vil gerne øve dem med eksempler fra lageret.
For preparation/help: Jeg har forberedt mig ved at … Jeg har brug for hjælp til …
For cooperation/goals: I gruppearbejdet bidrager jeg med … Mit næste mål er …
Replace the gaps with real experiences. Choose one small action: learn five terms, ask a clarification question per school day or practise an explanation with a colleague.''',
'''Inícios em dinamarquês: Jeg arbejder som logistikelev i IKEA. Mine opgaver er … Det går godt med … Et konkret eksempel er …
Para falar da dificuldade: Jeg synes, at de faglige begreber er udfordrende. Jeg vil gerne øve dem med eksempler fra lageret.
Preparação/ajuda: Jeg har forberedt mig ved at … Jeg har brug for hjælp til …
Colaboração/metas: I gruppearbejdet bidrager jeg med … Mit næste mål er …
Complete com experiências reais. Escolha uma ação pequena: aprender cinco termos, fazer uma pergunta de esclarecimento por dia ou treinar uma explicação com colega.''')

from article_lessons import expand_articles

expand_articles(PAGES, T, S)
