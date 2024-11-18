import gradio as gr
#from llm_call import GeminiLLM

from crewai import Agent, Task, Crew
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

# from seminar_edition_ai import upload_file_ex, predictContemplando, predictProclamando, predictFromInit, \
#    downloadSermonFile, fileAddresToDownload, predictQuestionBuild, predictDevotionBuild, predictArgumentQuestionBuild, \
#    contemplandoQuestion, proclamandoQuestion, llm, embed_model

HISTORY_ANSWER = ''

llmModel = None
def fileAddresToDownload():
    return True


def predictFromInit():
    return True

def downloadSermonFile():
    return True

def predictQuestionBuild():
    return True

def upload_file_ex(**kwargs):
    return True

def predictDevotionBuild(**kwargs):
    return True

def activeSermonGuideZone(KEY):
    #print("Button show " + buttonEvent.label)
    return {text_button: gr.update (interactive = True), question_option: [KEY]}

def showMessage(questionAnswer, KEY):
    if questionAnswer == None or questionAnswer == '' or len(questionAnswer) <= 7:
      raise gr.Error(f"You must write some answer or more longer {KEY}")
    else:
        try:
          return predictArgumentQuestionBuild(questionAnswer)
        except Exception as e:
            raise gr.Error(f" Error on call AI  {e}!!!")

contemplandoQuestion = {'DEVOCIONALMENTE':'Prueba', 'EXÉGESIS': 'Prueba 2', 'CRISTO':'Prueba 3', 'ARCO REDENTOR':'Prueba 4', 'EVANGELION':'Prueba 5', \
                         'EVANGELION_TWO':'Prueba 6','PÚBLICO':'Prueba 7'}

proclamandoQuestion = {'PÚBLICO':'Ejemplo 1','HISTORIA':'Ejemplo 2','EXPECTATIVAS':'Ejemplo 3','EXPECTATIVAS_TWO':'Ejemplo 4'}

with gr.Blocks() as demo:

    gr.Markdown("SermonLab AI Demo.")

    #llmModelState = gr.State([llmModel])

    with gr.Tab("CrewAi multi-agent Automtate Event Planning"):
        text_input = gr.Textbox(label="Tópico del sermón")

        text_output = gr.Textbox(label="Respuesta", lines = 10)

        text_button = gr.Button("Crear")

        text_download = gr.DownloadButton(
            label="Descargar",
            value = fileAddresToDownload,
            every=10
        )

        text_button.click(
            fn = predictFromInit,
            inputs =[ text_input],
            outputs = text_output
        )

        text_download.click(
            fn = downloadSermonFile,
            inputs = text_output
        )
    with gr.Tab("CrewAI Multi-agent outreach campaign"):
        with gr.Row():
            #Bibliografy about components
            # File (https://www.gradio.app/docs/gradio/file)
            # Download Button (https://www.gradio.app/docs/gradio/downloadbutton)
            with gr.Column():
                file_input_question = gr.File()
                upload_button_question = gr.UploadButton("Click to Upload a File", file_types=['.pdf'],
                                                         file_count="multiple")
            with gr.Column():
                temp_slider_question = gr.Slider(
                    minimum=1,
                    maximum=10,
                    value=1,
                    step=1,
                    interactive=True,
                    label="Preguntas",
                )
                text_output_question = gr.Textbox(label="Respuesta", lines=10)
        text_button_question = gr.Button("Crear guía de preguntas")
        text_download_question = gr.DownloadButton(
            label="Descargar",
            value=fileAddresToDownload,
            every=10
        )

        text_button_question.click(
            fn=predictQuestionBuild,
            outputs=text_output_question
        )

        upload_button_question.upload(upload_file_ex, inputs=upload_button_question,
                                      outputs=[file_input_question, text_output_question])

    with gr.Tab("CreawAI Multi-agent customer support automation"):
        with gr.Row():
            #Bibliografy about components
            # File (https://www.gradio.app/docs/gradio/file)
            # Download Button (https://www.gradio.app/docs/gradio/downloadbutton)

            with gr.Column():
                file_input_devotions = gr.File()
                upload_button_devotion = gr.UploadButton("Click to Upload a File", file_types=['.pdf'],
                                                         file_count="multiple")

            with gr.Column():
                temp_slider_question = gr.Slider(
                    minimum=1,
                    maximum=10,
                    value=1,
                    step=1,
                    interactive=True,
                    label="Cantidad",
                )
                text_output_devotions = gr.Textbox(label="Respuesta", lines=10)
        text_button_devotion = gr.Button("Crear")
        text_download_question = gr.DownloadButton(
            label="Descargar",
            value=fileAddresToDownload,
            every=10
        )

        text_button_devotion.click(
            fn=predictDevotionBuild,
            outputs=text_output_devotions
        )

        upload_button_devotion.upload(
            upload_file_ex,
            inputs=upload_button_devotion,
            outputs=
            [file_input_devotions, text_output_devotions]
        )
    with gr.Tab("CrewAI Multi-agent research an write an Article"):
        question_option = gr.State([])
        with gr.Accordion("Contemplando y Proclamando", open = False):
            checkButton = gr.Checkbox(
                value=False,
                label="Mantener historial"
            )
            with gr.Row():
                with gr.Tab("Contemplando"):
                    inbtwContemplando = gr.Button(f"Devocionalmente: {contemplandoQuestion['DEVOCIONALMENTE']}")
                    inbtwContemplandoOne = gr.Button(f"Exégesis: {contemplandoQuestion['EXÉGESIS']}")
                    inbtwContemplandoTwo = gr.Button(f"Cristo: {contemplandoQuestion['CRISTO']}")
                    inbtwContemplandoTree = gr.Button(f"Arco Redentor: {contemplandoQuestion['ARCO REDENTOR']}")
                    inbtwContemplandoFour = gr.Button(f"Evangelión: {contemplandoQuestion['EVANGELION']}")
                    inbtwContemplandoFourOne = gr.Button(f"Evangelión: {contemplandoQuestion['EVANGELION_TWO']}")

                with gr.Tab("Proclamando"):
                    inbtwProclamando = gr.Button(f"Público: {proclamandoQuestion['PÚBLICO']}")
                    inbtwProclamandoOne = gr.Button(f"Historia: {proclamandoQuestion['HISTORIA']}")
                    inbtwProclamandoTwo = gr.Button(f"Expectativas: {proclamandoQuestion['EXPECTATIVAS']}")
                    inbtwProclamandoTwoTwo = gr.Button(f"Expectativas: {proclamandoQuestion['EXPECTATIVAS_TWO']}")
        with gr.Row():
            with gr.Column(scale = 2):
                #Answer for Contemplando y Proclamando questions


                text_output_guia = gr.Textbox(label="Respuesta", lines = 10)


            with gr.Column(scale = 1, min_width = 200):
                text1 = gr.Textbox(visible = False)
                #Button for calling AI Help
                text_button = gr.Button("Buscar más información (IA)",
                                        min_width = 200,
                                        interactive = False
                                    )
                text2 = gr.Textbox(visible = False)
            with gr.Column(scale = 2):
                text_output_aiAnswer = gr.Textbox(label="Ayuda a mi respuesta", lines = 10)

        inbtwContemplando.click(
            fn = lambda x: activeSermonGuideZone(contemplandoQuestion['DEVOCIONALMENTE']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )

        inbtwContemplandoOne.click(
            fn = lambda x: activeSermonGuideZone(contemplandoQuestion['EXÉGESIS']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )

        inbtwContemplandoTwo.click(
            fn = lambda x: activeSermonGuideZone(contemplandoQuestion['CRISTO']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )

        inbtwContemplandoTree.click(
            fn = lambda x: activeSermonGuideZone(contemplandoQuestion['ARCO REDENTOR']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )

        inbtwContemplandoFour.click(
            fn = lambda x: activeSermonGuideZone(contemplandoQuestion['EVANGELION']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )

        inbtwContemplandoFourOne.click(
            fn = lambda x: activeSermonGuideZone(contemplandoQuestion['EVANGELION_TWO']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )

        #####---------------------------------------------------------------------------------------------------------
        inbtwProclamando.click(
            fn = lambda x: activeSermonGuideZone(proclamandoQuestion['PÚBLICO']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )


        inbtwProclamandoOne.click(
            fn = lambda x: activeSermonGuideZone(proclamandoQuestion['HISTORIA']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )

        inbtwProclamandoTwo.click(
            fn = lambda x: activeSermonGuideZone(proclamandoQuestion['EXPECTATIVAS']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )

        inbtwProclamandoTwoTwo.click(
            fn = lambda x: activeSermonGuideZone(proclamandoQuestion['EXPECTATIVAS_TWO']),
            inputs = inbtwContemplandoOne,
            outputs = [text_button, question_option]
        )


        text_button.click(fn = showMessage, inputs = [text_output_guia, question_option], outputs = text_output_aiAnswer)
    with gr.Tab("CrewAI Multi-agent research an write an Article"):
        gr.Markdown("##CrewAI Multi-agent research an write an Article")
    with gr.Tab("CrewAI Multi-agent collaboration for financial analysis"):
        gr.Markdown("##CrewAI Multi-agent collaboration for financial analysis")
    with gr.Tab("CrewAI Multi-agent to trailor job applications"):
        gr.Markdown("##CrewAI Multi-agent to trailor job applications")
    with gr.Tab("CrewAI Multi-agent hotel recommendations"):
        gr.Markdown('##CrewAI Multi-agent hotel recommendations')

if __name__ == "__main__":
   # llmBuilder = GeminiLLM()

    #embed_model = llmBuilder.getEmbeddingsModel()
    #global llmModel


    demo.launch(share=True)