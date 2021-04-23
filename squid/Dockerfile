FROM centos:7

RUN yum update -y && yum install -y squid && yum clean all

RUN /usr/lib64/squid/ssl_crtd -c -s /var/lib/ssl_db

CMD [ "/usr/sbin/squid", "-N", "-d", "1" ]
