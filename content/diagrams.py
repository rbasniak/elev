"""Exact SVG diagrams generated as native static assets, not raster images."""
from html import escape as E
from course import T

def supply(l,variant='supply'):
 labels=T(['Råvarer','Produktion','Distribution','Varehus','Kunde'],['Raw materials','Production','Distribution','Store','Customer'],['Matéria-prima','Produção','Distribuição','Loja','Cliente'])[l]
 if variant=='order':labels=T(['Kundeordre','ERP / kontrol','Pluk og pak','Transport','Levering'],['Customer order','ERP / checks','Pick and pack','Transport','Delivery'],['Pedido','ERP / conferir','Separar / embalar','Transporte','Entrega'])[l]
 caption=T('Forenklet model · varer frem, information begge veje og returvarer tilbage. Bekræft virksomhedens konkrete rute.','Simplified model · goods forward, two-way information and returned goods back. Confirm the actual company route.','Modelo simplificado · produtos adiante, informação nos dois sentidos e devolução de volta. Confirme a rota real.')[l]
 if variant=='order':caption=T('Kontrolpunkter: ordredata, beholdning, pluk, label og modtagelse. Ventetid kan opstå ved mangel, batch og transportafgang.','Checkpoints: order data, stock, picking, labels and receipt. Waiting can arise at shortages, batches and departures.','Conferências: pedido, estoque, separação, etiqueta e recebimento. Espera pode surgir em faltas, lotes e saídas.')[l]
 s='<figure class="study-section answer" data-anchor="diagram-'+variant+'"><div class="diagram-scroll"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 220" role="img" aria-label="'+E(caption)+'"><defs><marker id="arr-'+l+'-'+variant+'" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#17675f"/></marker></defs>'
 marker='url(#arr-'+l+'-'+variant+')'
 for i,label in enumerate(labels):
  x=10+i*170
  s+=f'<rect x="{x}" y="40" width="145" height="65" rx="10" fill="#edf5ef" stroke="#a7cabc"/><text x="{x+72.5}" y="78" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#172e40">{E(label)}</text>'
  if i<4:s+=f'<path d="M{x+145} 72H{x+165}" stroke="#17675f" stroke-width="2" marker-end="{marker}"/>'
 s+=f'<path d="M82 145H762" stroke="#17675f" stroke-width="2" stroke-dasharray="5 5" marker-start="{marker}" marker-end="{marker}"/>'
 info=T('Information / koordinering','Information / coordination','Informação / coordenação')[l]
 s+=f'<text x="425" y="173" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#586b75">{E(info)}</text></svg></div><figcaption>{E(caption)}</figcaption></figure>'
 return s
