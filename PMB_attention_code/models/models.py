
def create_model(opt):
    model = None
    print(opt.model)
    if opt.model == 'Organ_attention':
        assert(opt.dataset_mode == 'unaligned')
        from .Organ_attention import Organ_attention
        model = Organ_attention()
    else:
        raise ValueError("Model [%s] not recognized." % opt.model)
    
    print (opt.model)
    print (model)
    model.initialize(opt)
    print("model [%s] was created" % (model.name()))
    return model
