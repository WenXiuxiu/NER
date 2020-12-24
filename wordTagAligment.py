# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import re
import pickle
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
        for idx, txtpath,annpath in self.getSourceFiles(FilesPath,'txt'):
            with open(txtpath,encoding='utf-8') as txtf:
                contents = txtf.read()
                if(len(contents)<1):
                    return
                wordlist = list(contents)
                taglist = ['O']*len(wordlist)
                with open(annpath, encoding='utf-8') as annf:
                    print('processing',idx)
                    for line in annf:
                        formatFlag, formatedRes = self.formatLine(line)
                        if( formatFlag):
                            begin = int(formatedRes[1])
                            end = int(formatedRes[2])
                            if(end-begin>2):
                                taglist[begin:end] = ['I_'+formatedRes[0]]*(end-begin)
                                taglist[begin] = 'B_'+formatedRes[0]
                                taglist[end-1] = 'E_'+formatedRes[0]
                            else:
                                taglist[begin] = 'S_'+formatedRes[0]
                    with open(os.path.join(self.targetFloder,idx+'.pkl') ,'wb') as targetfile:
                        pickle.dump(list(zip(wordlist,taglist)),targetfile)
                        
    def formatLine(self,line):
        objgroups = re.match(r'T\d*\t(\S*) (\d*) (\d*)\t(.+)',line)
        if(objgroups==None):
            return [False,[]]
        else:
            return [True,list(objgroups.groups())]
        
