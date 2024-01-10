def extract_domain(url):
    #remove the scheme(http:// or https://)
    url = url.split('://')[-1]

    #Remove the subdomain(www.)
    url = url.replace('www.', '')

    #Exraction the domain name
    domain_parts = url.split('.')

    #check if the domain has a subdomain
    if len(domain_parts) > 2:
        domain_name = domain_parts[-2]
    else:
        domain_name = domain_parts[0]

    return domain_name