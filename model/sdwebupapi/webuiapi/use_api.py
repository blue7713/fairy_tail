import webuiapi
from gpt_prompt import gen

# create API client
api = webuiapi.WebUIApi()

# create API client with custom host, port
api = webuiapi.WebUIApi(host='127.0.0.1', port=7860, sampler='Euler a', steps=20)

result1 = api.txt2img(prompt=gen("아기 공룡이 노란 꽃밭은 나풀나풀 날아다녀요"), 
                      negative_prompt="",
                      seed=5555, 
                      cfg_scale=6.5, 
                      denoising_strength=0.6,
                      batch_size=1,
                      steps=20,
                      save_images=True,
                      styles=["anime"]
                    )

print()
# images contains the returned images (PIL images)
result1.image.save("output_image.png")

# txt2img parameters
# {
#   "prompt": "",
#   "negative_prompt": "",
#   "styles": [
#     "string"
#   ],
#   "seed": -1,
#   "subseed": -1,
#   "subseed_strength": 0,
#   "seed_resize_from_h": -1,
#   "seed_resize_from_w": -1,
#   "sampler_name": "string",
#   "batch_size": 1,
#   "n_iter": 1,
#   "steps": 50,
#   "cfg_scale": 7,
#   "width": 512,
#   "height": 512,
#   "restore_faces": true,
#   "tiling": true,
#   "do_not_save_samples": false,
#   "do_not_save_grid": false,
#   "eta": 0,
#   "denoising_strength": 0,
#   "s_min_uncond": 0,
#   "s_churn": 0,
#   "s_tmax": 0,
#   "s_tmin": 0,
#   "s_noise": 0,
#   "override_settings": {},
#   "override_settings_restore_afterwards": true,
#   "refiner_checkpoint": "string",
#   "refiner_switch_at": 0,
#   "disable_extra_networks": false,
#   "comments": {},
#   "enable_hr": false,
#   "firstphase_width": 0,
#   "firstphase_height": 0,
#   "hr_scale": 2,
#   "hr_upscaler": "string",
#   "hr_second_pass_steps": 0,
#   "hr_resize_x": 0,
#   "hr_resize_y": 0,
#   "hr_checkpoint_name": "string",
#   "hr_sampler_name": "string",
#   "hr_prompt": "",
#   "hr_negative_prompt": "",
#   "sampler_index": "Euler",
#   "script_name": "string",
#   "script_args": [],
#   "send_images": true,
#   "save_images": false,
#   "alwayson_scripts": {}
# }