# demo-webapp
The demo webapp originally from https://github.com/jfclere/tomcat-openshift
Used as demo webapp example in the jws-image-operator.

The servlet is /demo so it can be reached with http://hostname/demo-1.0/demo

To build the application, execute

```sh
mvn package
# builds  `target/demo-1.0.war`
```

