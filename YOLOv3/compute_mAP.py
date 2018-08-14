from voc_eval import voc_eval
 
print voc_eval('./results/{}.txt', '/data/headdata/data/VOCdevkit/headdata/Annotations/{}.xml', '/data/headdata/data/VOCdevkit/headdata/ImageSets/Main/test.txt','person', '.')

