#simple program to connect with OpenSearch server using Elasticsearch Client.
#OpenSearch 1.1 Docker is used as OpenSearch server
#Elasticsearch python client version 7.13.4 
#For ref https://opensearch.org/docs/clients/index/#opensearch-client-compatibility
#
#Issue
#OpenSearch server on Docker available one opensearch.org is configured with Https by default. 
#urllib3.exceptions.NewConnectionError are possoble if client request is not correctly configured
#Erros like, [Errno 111] Connection refused, <urllib3.connection.VerifiedHTTPSConnection object can occure
#The following can be used to successfully establish connection with OpenSearch Server v1.1 running on Docker using Elasticsearch python client

from elasticsearch import Elasticsearch

def main():   

   es = Elasticsearch(
        scheme="https",
        hosts=[ { 'port': 9200, 'host': 'localhost' } ],
        verify_certs=False, 
        ssl_show_warn=False,
        http_auth=("username", "password") # replace with your username then password
   )
   print(es.info())



if __name__ == '__main__':
    main()
