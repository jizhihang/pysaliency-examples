import pysaliency

pysaliency.get_mit1003(location='cache/datasets')
pysaliency.get_mit1003_onesize(location='cache/datasets')
pysaliency.get_mit300(location='cache/datasets')
#pysaliency.get_SALICON_train(location='cache/datasets')
#pysaliency.get_SALICON_val(location='cache/datasets')
#pysaliency.get_SALICON_test(location='cache/datasets')
#pysaliency.get_iSUN_training(location='cache/datasets')
m1 = pysaliency.AIM(location='cache/model_sources', cache_location='cache/model_caches/AIM/')
m2 = pysaliency.GBVSIttiKoch(location='cache/model_sources', cache_location='cache/model_caches/GBVSIttiKoch')

#s,f = pysaliency.get_mit1003(location='cache/datasets')
#for ss in s:
#    m1.saliency_map(ss)

