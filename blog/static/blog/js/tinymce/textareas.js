tinymce.init({
  selector: 'textarea',
  language: 'zh_CN',
  height: 500,
  theme: 'modern',
  plugins: [
    'advlist autolink lists link image charmap print preview hr anchor pagebreak',
    'searchreplace wordcount visualblocks visualchars code fullscreen',
    'insertdatetime media nonbreaking save table contextmenu directionality',
    'emoticons template paste textcolor colorpicker textpattern imagetools codesample'
  ],
  toolbar1: 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
  toolbar2: 'print preview media | forecolor backcolor emoticons | codesample',
  image_advtab: true,
  templates: [
    { title: 'Test template 1', content: 'Test 1' },
    { title: 'Test template 2', content: 'Test 2' }
  ],
  image_caption: true,
  media_live_embeds: true,
  imagetools_cors_hosts: ['tinymce.com', 'codepen.io'],
  content_css: [
    '//cdnjs.cloudflare.com/ajax/libs/prism/0.0.1/prism.css',
    '//www.tinymce.com/css/codepen.min.css'
  ]
 });