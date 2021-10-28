from __future__ import unicode_literals, print_function
import spacy
from spacy.training import Example
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication
import os
import random
import time


class Model_Training(QtCore.QThread):
    #This is the signal that will be emitted during the processing.
    #By including int as an argument, it lets the signal know to expect
    #an integer argument when emitting.
    updateProgress = QtCore.Signal(int)

    # truyền tham số là đường dẫn tới file train
    def train_model(self,df_train_input):

            # determine if application is a script file or frozen exe
            # if getattr(sys, 'frozen', False):

            #    root_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.executable)))

            # elif __file__:

            #     root_path = os.path.dirname(os.path.abspath(__file__))

            model = os.path.abspath('')  + '\\en_core_web_lg\\en_core_web_lg-3.1.0'
            output_dir= os.path.abspath('')  + '\\ner'
            # train_file_dir = os.path.abspath('')  + '\\Train_data\\Train_data.xlsx'
            n_iter=100

            # start_time = time.time()

            if model is not None:
                nlp = spacy.load(model)  
                # print("Loaded model '%s'" % model)
            else:
                nlp = spacy.blank('en')  
                # print("Created blank 'en' model")

            #set up the pipeline

            if 'ner' not in nlp.pipe_names:
                ner = nlp.create_pipe('ner')
                nlp.add_pipe(ner, last=True)
            else:
                ner = nlp.get_pipe('ner')

            # set up training data
            df_training = df_train_input[df_train_input['Trained'] != 'X']
            df_training = df_training.reset_index(drop=True)

            if len(df_training) > 0:
                training_data = []
                # chuẩn bị dữ liệu train
                for idx in range(len(df_training)):
                    entity_name = df_training.loc[idx, "Entity name"]
                    entity_label = df_training.loc[idx, "Entity label"]
                    training_enity = (entity_name, {'entities': [(0, len(entity_name), entity_label)]})
                    training_data.append(training_enity)

                # add label
                for _, annotations in training_data:
                    for ent in annotations.get('entities'):
                        ner.add_label(ent[2])


                other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
                with nlp.disable_pipes(*other_pipes):  # only train NER
                    optimizer = nlp.create_optimizer()
                    for itn in range(n_iter):

                        # emit signal to main_GUI
                        QApplication.processEvents()
                        self.updateProgress.emit(itn + 1)
                        time.sleep(0.2)

                        random.shuffle(training_data)
                        losses = {}
                        for batch in spacy.util.minibatch(training_data, size=2):
                            for text, annotations in batch:
                                doc = nlp.make_doc(text)
                                example = Example.from_dict(doc, annotations)
                                nlp.update(
                                    [example],   
                                    drop=0.5,  
                                    sgd=optimizer,
                                    losses=losses)

                # print("--- %s seconds ---" % round(time.time() - start_time, 2))
                #Save model
                if output_dir is not None:
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                    nlp.to_disk(output_dir)


                df_train_input['Trained'] = 'X'
                return df_train_input



