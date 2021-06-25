FROM python:3

WORKDIR /tmp

RUN pip install --no-cache-dir sigproSS
COPY spss_genInstall_GRCh37.py .
RUN python spss_genInstall_GRCh37.py
COPY spss.py /usr/local/bin/
RUN sed -i 's/\/Signatures/\/signatures/' /usr/local/lib/python3.9/site-packages/sigproSS/spss.py
