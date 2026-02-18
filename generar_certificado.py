"""
Script para generar certificado SSL autofirmado para PWA
"""
from OpenSSL import crypto
import os

def generate_self_signed_cert(cert_file="cert.pem", key_file="key.pem"):
    """Genera un certificado SSL autofirmado"""
    
    # Crear par de claves
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)
    
    # Crear certificado
    cert = crypto.X509()
    cert.get_subject().C = "ES"
    cert.get_subject().ST = "Estado"
    cert.get_subject().L = "Ciudad"
    cert.get_subject().O = "Entrenamiento Voleibol"
    cert.get_subject().OU = "PWA"
    cert.get_subject().CN = "Voleibol Pro"
    
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365*24*60*60)  # Válido por 1 año
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha256')
    
    # Guardar certificado y clave
    with open(cert_file, "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    
    with open(key_file, "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    
    print(f"✅ Certificado creado: {cert_file}")
    print(f"✅ Clave privada creada: {key_file}")
    print()
    print("🔒 El servidor ahora usará HTTPS")
    print("⚠️  Chrome mostrará advertencia de 'No seguro' - es normal")
    print("   Haz clic en 'Avanzado' → 'Continuar al sitio'")

if __name__ == "__main__":
    print("🔐 Generando certificado SSL autofirmado...")
    print()
    generate_self_signed_cert()
    print()
    print("🎉 ¡Listo! Ahora Chrome detectará la app como PWA instalable")
