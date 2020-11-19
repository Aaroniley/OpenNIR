import os
path = r'/home/Bio/liuzhiqiang/OpenNIR'
dir_list = []
for dirpath,dirnames,filenames in os.walk(path):
    for filename in filenames:
        dir_list.append(os.path.join(dirpath,filename)+'\n')
with open('dir_list.txt','w',encoding='utf-8') as f:
    f.writelines(dir_list)
 

# ranker=conv_knrm 
./
ranker.pretrained_kernels=True
# vocab=wordvec_hash
vocab.source=convknrm
vocab.variant=convknrm-bing
dataset=antique
# pipeline.val_metric=mrr_rel-3
# ranker.qlen=30
# ranker.dlen=475
./train
./valid
./test
# test_ds=antique
test_ds.subset=test
# test_ds.rankfn=bm25_k1-1.4_b-0.40
# test_ds.ranktopk=50
# test_pred.measures=map_rel-3,mrr_rel-3,p_rel-3@1,p_rel-3@3,judged@10
# train_ds=antique
# train_ds.subset=train
# train_ds.ranktopk=100
# train_ds.rankfn=bm25_k1-1.4_b-0.40
# trainer.pos_minrel=3
valid_ds=antique
valid_ds.subset=valid
# valid_ds.ranktopk=20
# valid_ds.rankfn=bm25_k1-1.4_b-0.40
# valid_pred.measures=map_rel-3,mrr_rel-3,p_rel-3@1,p_rel-3@3,p_rel-3@10,ndcg_gain-1=0:2=1:3=2:4=3@1,ndcg_gain-1=0:2=1:3=2:4=3@3,ndcg_gain-1=0:2=1:3=2:4=3@10,judged@10
# pipeline.val_metric=mrr_rel-3
vocab      wordvec_hash                                                        
--------------------------------------------------------------------------------
 source     fasttext      |  variant      wiki-news-300d-1M  |  train     False 
 hashspace  1000          |  init_stddev  0.5                |  log_miss  False 

 train_ds  antique                                                
------------------------------------------------------------------
 rankfn    bm25_k1-1.4_b-0.40  |  subset  train  |  ranktopk  100 

 ranker            conv_knrm                                                                                                                                      
------------------------------------------------------------------------------------------------------------------------------------------------------------------
 qlen              30                                                |  dlen                475                                            |  add_runscore  False 
 mus               -0.9,-0.7,-0.5,-0.3,-0.1,0.1,0.3,0.5,0.7,0.9,1.0  |  sigmas              0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.001  |  grad_kernels  True  
 max_ngram         3                                                 |  crossmatch          True                                           |  conv_filters  128   
 combine_channels  False                                             |  pretrained_kernels  False                                                                 

 trainer     pairwise                                                           
--------------------------------------------------------------------------------
 batch_size  16         |  batches_per_epoch  32     |  grad_acc_batch  0       
 optimizer   adam       |  lr                 0.001  |  gpu             True    
 gpu_determ  True       |  encoder_lr         0.0    |  lossfn          softmax 
 pos_source  intersect  |  neg_source         run    |  sampling        query   
 pos_minrel  3          |  unjudged_rel       0      |  num_neg         1       
 margin      0.0                                                                

 valid_ds  antique                                               
-----------------------------------------------------------------
 rankfn    bm25_k1-1.4_b-0.40  |  subset  valid  |  ranktopk  20 

 valid_pred  reranker                                                                                                                                                                                           
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 batch_size  64        |  gpu            True  |  gpu_determ  True                                                                                                                                              
 preload     False     |  run_threshold  0     |  measures    map_rel-3,mrr_rel-3,p_rel-3@1,p_rel-3@3,p_rel-3@10,ndcg_gain-1=0:2=1:3=2:4=3@1,ndcg_gain-1=0:2=1:3=2:4=3@3,ndcg_gain-1=0:2=1:3=2:4=3@10,judged@10 
 source      run                                                                                                                                                                                                

 test_ds  antique                                              
---------------------------------------------------------------
 rankfn   bm25_k1-1.4_b-0.40  |  subset  test  |  ranktopk  50 

 test_pred   reranker                                                                                           
----------------------------------------------------------------------------------------------------------------
 batch_size  64        |  gpu            True  |  gpu_determ  True                                              
 preload     False     |  run_threshold  0     |  measures    map_rel-3,mrr_rel-3,p_rel-3@1,p_rel-3@3,judged@10 
 source      run                                                                                                

 pipeline      default                                                   
-------------------------------------------------------------------------
 max_epoch     1000       |  early_stop     20     |  warmup       -1    
 val_metric    mrr_rel-3  |  purge_weights  True   |  test         False 
 initial_eval  False      |  skip_ds_init   False  |  only_cached  False 