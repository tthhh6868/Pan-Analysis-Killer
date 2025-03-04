import asyncio
import aiodns
import random
import optparse
import platform

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
resolver = aiodns.DNSResolver(loop=loop)

async def query(name, query_type):
    try:
        return await resolver.query(name, query_type)
    except aiodns.error.DNSError as e:
        return f"查询失败: {name} - {str(e)}"

def random_to_A(main_domain):
    total = []
    # 随机循环五次
    for i in range(5):
        sub_domain = "".join(random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(8, 12)))
        res = query(sub_domain + "." + main_domain, 'A')
        result = loop.run_until_complete(res)
        total.append(result)
    return total

def random_to_cname(sub_domain):
    try:
        res = query(sub_domain, 'CNAME')
        result = loop.run_until_complete(res)
        return result
    except aiodns.error.DNSError as e:
        return f"查询失败: {sub_domain} - {str(e)}"

if __name__ == '__main__':
    parser = optparse.OptionParser("%prog " + "[options] [domain]")
    parser.add_option('-a', action="store", dest='main_domain', type='string', help='')
    parser.add_option('-c', action="store", dest='sub_domain', type='string', help='')
    (options, args) = parser.parse_args()
    main_domain = options.main_domain
    sub_domain = options.sub_domain
    if main_domain:
        print(str(random_to_A(main_domain)).replace("],", "],\n"))
    elif sub_domain:
        print(str(random_to_cname(sub_domain)).replace("<", "\n<"))