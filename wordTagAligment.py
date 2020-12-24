# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import re
class wordTagAligment():
    def __init__(self,targetFolder):
        self.targetFloder = targetFolder
        if(not os.path.isdir(self.targetFloder)):
            os.makedirs(self.targetFloder)
            
    def getSourceFiles(self,FilesPath,filetag):
        if(not os.path.isdir(FilesPath)):
            print('The filespath is not correct!')
            return
        txtfiles = os.listdir(FilesPath)
        for f in txtfiles:
            if f.endswith(filetag):
                annfile = os.path.join(FilesPath,f[:-3]+'ann')
                if os.path.exists(annfile):
                    yield [f[:-3], os.path.join(FilesPath,f),annfile]
        return
    def alignWordTag(self,FilesPath):
        i = 1
        for idx, txtpath,annpath in self.getSourceFiles(FilesPath,'txt'):
            with open(txtpath,encoding='utf-8') as txtf:
                contents = txtf.read()
                if(len(contents)<1):
                    return
                wordlist = list(contents)
                taglist = ['O']*len(wordlist)
                with open(annpath,encoding='utf-8') as annf:
                    for line in annf:
                        print(line)
                    
    
    def extractFromLine(self,line):
        objgroups = re.match(r'T\d*\t(\S*) (\d*) (\d*)\t(.+)',line)
        if(objgroups==None):
            return [False, []]
        else:
            return [True, list(objgroups.groups())]
        
        
                        

w = wordTagAligment('/home/alice/coding/python/ner_mmc/dataWordTagligment') 
print(w.extractFromLine('T357    Reason 4396 4405        垂体内分泌细胞毁损'))
            
    
        
        