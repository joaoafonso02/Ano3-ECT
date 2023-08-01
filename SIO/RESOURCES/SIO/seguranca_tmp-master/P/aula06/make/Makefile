WGET = wget --no-check-certificate
KEYTOOL = keytool
JAVAC = javac

KS_PWD = password

CC_ROOTS = \
    https://www.digicert.com/CACerts/BaltimoreCyberTrustRoot.crt \
    https://pki.multicert.com/cert/MULTICERT_CA/mca_001_2.cer \
    https://www.scee.gov.pt/media/6944/ecraizestado002.zip

CC_STATE_ROOTS = \
    https://www.scee.gov.pt/media/7017/ecraizestado.zip

CC_CERTS = 1 2 3 4 5 6 # Add more number if needed
CC_CERT_FILES = $(foreach n, $(CC_CERTS), Cartao-de-Cidadao-00$(n).cer)

CC_SIGN_CERTS = 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 # Add more number if needed
CC_SIGN_CERT_FILES = $(foreach n, $(CC_SIGN_CERTS), EC-de-Assinatura-Digital-Qualificada-do-Cartao-de-Cidadao-00$(n).cer)

CC_AUTH_CERTS = 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 # Add more number if needed
CC_AUTH_CERT_FILES = $(foreach n, $(CC_AUTH_CERTS), EC-de-Autenticacao-do-Cartao-de-Cidadao-00$(n).cer)

CC_ALL_CERT_FILES = \
	$(foreach c, $(CC_ROOTS), $(notdir $c)) \
	$(foreach c, $(CC_STATE_ROOTS), $(notdir $c)) \
	$(CC_CERT_FILES) \
	$(CC_SIGN_CERT_FILES) \
	$(CC_AUTH_CERT_FILES)
CCKS = CC_KS

all: update PEM

update:
	@rm newCerts; \
	for i in $(CC_ROOTS) $(CC_STATE_ROOTS); do \
	    filename=`basename $$i`; \
            alias=`echo $$filename | \
			sed -e s/.cer//g | \
			sed -e s/.der//g | \
			sed -e s/.crt//g | \
			sed -e s/.zip//g | \
			sed -e s/-//g | \
			tr A-Z a-z`; \
	    echo "Check alias $$alias"; \
	    $(KEYTOOL) -exportcert -alias $$alias -storepass $(KS_PWD) -noprompt -keystore $(CCKS) > /dev/null || \
	    ( \
		echo "Get certificate from $$i"; \
	    	$(WGET) $$i -o /dev/null -O $$filename && \
		( \
		    if [ "$$alias.zip" = "$$filename" ]; then \
			unzip -o $$filename; \
			filename=`unzip -t $$filename | grep testing | awk '{print $$2}'`; \
		    fi; \
		    echo $$filename >> newCerts; \
		) \
	    ) \
	done; \
	for i in $(CC_CERT_FILES); do \
	    filename=`basename $$i`; \
            alias=`echo $$filename | \
			sed -e s/.cer//g | \
			sed -e s/.der//g | \
			sed -e s/.crt//g | \
			sed -e s/-//g | \
			tr A-Z a-z`; \
	    echo "Check alias $$alias"; \
	    $(KEYTOOL) -exportcert -alias $$alias -storepass $(KS_PWD) -noprompt -keystore $(CCKS) > /dev/null || \
	    ( \
		u=`echo $$i | sed -e s/-/%20/g`; \
	    	$(WGET) https://pki.cartaodecidadao.pt/publico/certificado/cc_ec_cidadao/$$u -o /dev/null -O $$filename && \
		( \
		    s=`echo $$i | sed -e s/-/\ /g`; \
		    mv "$$s" $$i; \
		    echo $$filename >> newCerts; \
		) \
	    ) \
	done; \
	for i in $(CC_SIGN_CERT_FILES); do \
	    filename=`basename $$i`; \
            alias=`echo $$filename | \
			sed -e s/.cer//g | \
			sed -e s/.der//g | \
			sed -e s/.crt//g | \
			sed -e s/-//g | \
			tr A-Z a-z`; \
	    echo "Check alias $$alias"; \
	    $(KEYTOOL) -exportcert -alias $$alias -storepass $(KS_PWD) -noprompt -keystore $(CCKS) > /dev/null || \
	    ( \
		u=`echo $$i | sed -e s/-/%20/g`; \
	    	$(WGET) https://pki.cartaodecidadao.pt/publico/certificado/cc_ec_cidadao_assinatura/$$u -o /dev/null -O $$filename && \
		( \
		    s=`echo $$i | sed -e s/-/\ /g`; \
		    mv "$$s" $$i; \
		    echo $$filename >> newCerts; \
		) \
	    ) \
	done; \
	for i in $(CC_AUTH_CERT_FILES); do \
	    filename=`basename $$i`; \
            alias=`echo $$filename | \
			sed -e s/.cer//g | \
			sed -e s/.der//g | \
			sed -e s/.crt//g | \
			sed -e s/-//g | \
			tr A-Z a-z`; \
	    echo "Check alias $$alias"; \
	    $(KEYTOOL) -exportcert -alias $$alias -storepass $(KS_PWD) -noprompt -keystore $(CCKS) > /dev/null || \
	    ( \
		u=`echo $$i | sed -e s/-/%20/g`; \
	    	$(WGET) https://pki.cartaodecidadao.pt/publico/certificado/cc_ec_cidadao_autenticacao/$$u -o /dev/null -O $$filename && \
		( \
		    s=`echo $$i | sed -e s/-/\ /g`; \
		    mv "$$s" $$i; \
		    echo $$filename >> newCerts; \
		) \
	    ) \
	done; \
	[ -f newCerts ] && \
	    for i in `cat newCerts`; do \
		alias=`echo $$i | \
		    sed -e s/.cer//g | \
		    sed -e s/.der//g | \
		    sed -e s/.crt//g | \
		    sed -e s/-//g`; \
		echo -n "Certificate with alias" $$alias ": "; \
		$(KEYTOOL) -importcert  -storepass $(KS_PWD) -noprompt -keystore $(CCKS) -file $$i -alias "$$alias"; \
	    done; \
	echo "done"

PEM:
	@for i in `ls *.cer *.der *.crt`; do \
	    echo $$i; \
	    name=`echo $$i | \
		sed -e s/.cer//g | \
		sed -e s/.der//g | \
		sed -e s/.crt//g`; \
	    if file $$i | grep PEM; then \
	        mv $$i $$name.pem; \
		openssl x509 -in $$name.pem -inform PEM -out $$i -outform DER; \
	    else \
		if [ ! -f  $$name.pem ]; then \
		    echo "generate $$name.pem"; \
		    openssl x509 -in $$i -inform DER -out $$name.pem -outform PEM; \
		fi; \
	    fi; \
	done

