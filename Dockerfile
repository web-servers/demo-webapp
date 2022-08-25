FROM quay.io/jfclere/image-builder-jws
LABEL Description="Tomcat webapp image to use with the JWS operator"
VOLUME /tmp

RUN uname -a

# The script just tests that the builder is build a war nothing else (adjust it to your need)
RUN (cd /tmp; git clone https://github.com/jfclere/demo-webapp.git; cd demo-webapp; git checkout jakartaEE; mvn install; if [ -d /deployments ]; then cp target/demo-1.0.war /deployments/ROOT.war; fi)
