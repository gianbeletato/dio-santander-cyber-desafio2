# 🛡️ Projeto de Cibersegurança 2025 - DIO & Santander

Este repositório contém dois projetos desenvolvidos como parte do **Desafio de Cibersegurança 2025** promovido pela [Digital Innovation One (DIO)](https://www.dio.me) em parceria com o **Santander**. O objetivo é simular o comportamento de malwares em ambiente seguro, utilizando Python, e refletir sobre medidas de defesa e prevenção.

---

## 📁 Estrutura do Projeto

- `projeto_ransomware/`  
  Simulação de um ransomware simples que criptografa arquivos de teste e exibe uma mensagem de "resgate". Inclui também o script de descriptografia com base na chave gerada.

- `projeto_keylogger/`  
  Captura de teclas em segundo plano e registro em arquivo `.txt`. Com melhoria para envio automático por e-mail, simulando comportamento furtivo.

---

## 🔐 Ransomware Simulado

### Funcionalidades
- Geração de arquivos de teste
- Criptografia com chave simétrica
- Mensagem de resgate simulada
- Script de descriptografia com validação da chave

### Observações
> Este projeto é **educacional** e não representa ameaça real. Todos os testes foram realizados em ambiente controlado.

---

## 🎯 Keylogger Simulado

### Funcionalidades
- Captura de teclas em tempo real
- Registro em arquivo `.txt`
- Execução oculta (furtividade)
- Envio periódico por e-mail (SMTP)

### Observações
> O envio de e-mails requer configuração de credenciais e permissões específicas. Recomenda-se utilizar contas de teste.

---

## 🧠 Reflexões sobre Defesa e Prevenção

Durante o desenvolvimento, foram estudadas diversas medidas de proteção contra malwares:

- **Antivírus**: detecção baseada em assinaturas e comportamento
- **Firewall**: bloqueio de conexões suspeitas
- **Sandboxing**: execução isolada de arquivos desconhecidos
- **Conscientização do Usuário**: educação sobre phishing, engenharia social e boas práticas

> A segurança cibernética depende tanto de tecnologia quanto de comportamento humano. Este projeto reforça a importância de entender como ameaças operam para melhor combatê-las.

---

## ⚠️ Aviso Legal

Este projeto é **exclusivamente educacional** e não deve ser utilizado para fins maliciosos. O uso indevido de técnicas aqui demonstradas pode violar leis e políticas de segurança.

---

### Pré-requisitos
- Python 3.8+
- Bibliotecas: `cryptography`, `pynput`, `smtplib`, `email`
