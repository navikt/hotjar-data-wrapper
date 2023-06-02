# %%
import os

import hotjar_data_wrapper.hotjar_api as hot

# %%
username = os.environ["username"]
password = os.environ["password"]
site_id = os.environ["account"]
survey_id = os.environ["survey_id"]
# %%
status = hot.login_hotjar(username=username, password=password)
status.content
# %%
questions = hot.get_survey_questions(
    survey_id=survey_id, site_id=site_id, username=username, password=password
)
questions.content
# %%
meta = hot.get_survey_metadata(
    survey_id=survey_id, site_id=site_id, username=username, password=password
)
meta.status_code  # 200
meta.content  # prints content
# %%
all_surveys = hot.get_list_all_surveys(
    site_id=site_id, username=username, password=password
)
all_surveys.content
# %%
hot.get_all_surveys_metadata(
    path="data/hotjar surveys",
    surveys_list=ids,
    site_id=site_id,
    username=username,
    password=password,
)
