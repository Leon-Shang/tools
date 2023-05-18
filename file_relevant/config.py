c = get_config()

c.NotebookApp.contents_manager_class = "jupyter_server.services.contents.largefilemanager.LargeFileManager"
c.Exporter.preprocessors = ['extract_attachments_preprocessor.ExtractAttachmentsPreprocessor']

print(c)