                
                const imageBox=document.getElementById('image-box');
                const imageForm=document.getElementById('image-Form');
                const imagePreview = document.getElementById('imagePreview');
                console.log(imageForm);
                const imageInput=document.getElementById('photo');
                const saveButton = document.getElementById('saveButton');
            
                imageInput.addEventListener('change', (event) => {
                    const file = event.target.files[0];
                    if (file) {
                      const reader = new FileReader();
                      reader.onload = () => {
                        imagePreview.src = reader.result;
                        imagePreview.style.display = 'block'; // Mostrar a imagem
                        saveButton.style.display = 'block'; // Mostrar o botão salvar
                
                        // Inicializar o cropper ou atualizar caso já exista
                        const cropper = new Cropper(imagePreview, {
                          aspectRatio: 16 / 9,
                        });
                        console.log(cropper);
                        saveButton.addEventListener('click', () => {
                            if (cropper) {
                              cropper.getCroppedCanvas().toBlob((blob) => {
                                const formData = new FormData();
                                formData.append('croppedImage', blob);
                                console.log(cropper);
                        
                                fetch('/upload_photo', {
                                  method: 'POST',
                                  body: formData,
                                })
                                  .then((response) => response.json())
                                  .then((data) => {
                                    alert('Foto salva com sucesso!');
                                    console.log('Resposta do servidor:', data);
                                  })
                                  .catch((error) => {
                                    console.error('Erro ao salvar:', error);
                                  });
                              });
                            }
                          });
                      };
                      reader.readAsDataURL(file);

                     
                    }

                    
                  });
             
            
                