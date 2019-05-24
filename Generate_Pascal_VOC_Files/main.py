import build_pascal_voc

pascal_voc_data = '''
                    [
                                        {
                                            "folder":"folder",
                                            "filename": "1.jpg",
                                            "path":"path",
                                            "source":{"database":"database"},
                                            "size":{"width":256,"height":256,"depth":3},
                                            "segmented":0,
                                            "objects":[{"name":"name","pose":"pose","truncated":"0","difficult":0,"occluded":"occluded","bndbox":{"xmin":3,"ymin":3,"xmax":33,"ymax":33}},{"name":"name","pose":"pose","truncated":"0","difficult":0,"occluded":"occluded","bndbox":{"xmin":3,"ymin":3,"xmax":33,"ymax":33}}]

                                        },
                                        {
                                            "folder":"folder",
                                            "filename": "2.jpg",
                                            "path":"path",
                                            "source":{"database":"database"},
                                            "size":{"width":256,"height":256,"depth":3},
                                            "segmented":0,
                                            "objects":[{"name":"name","pose":"pose","truncated":"0","difficult":0,"occluded":"occluded","bndbox":{"xmin":3,"ymin":3,"xmax":33,"ymax":33}},{"name":"name","pose":"pose","truncated":"0","difficult":0,"occluded":"occluded","bndbox":{"xmin":3,"ymin":3,"xmax":33,"ymax":33}}]
                                        }
                    ]

                '''


'''Call the function to  build pascal formart'''
build_pascal_voc.build_pascal_voc_formart(pascal_voc_data)
