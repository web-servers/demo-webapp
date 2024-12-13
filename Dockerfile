FROM quay.io/jfclere/image-builder-jws
LABEL Description="Tomcat webapp image to use with the JWS operator"
VOLUME /tmp

RUN uname -a

RUN git clone https://github.com/web-servers/demo-webapp.git

RUN (cd demo-webapp; mvn install; cp target/demo-1.0.war /deployments/ROOT.war)

