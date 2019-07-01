<submit-homework-github>
    <style>
        .commit {
            width: 70%;
        }

        .commit-header {
            width: 100%;
            display: flex;
            flex-direction: row;
        }

        .sha {
            color: #70c4ff;
            font-weight: bold;
            width: 15%;
        }

        .commit-message {
            color: #636363;
            width: 80%;
        }

        .commit-date {
            color: #999999;
        }

        /* this will only style the popup if inline is true */
        .popup {
{#            color: #FF0000 !important;#}
        }

    </style>

    <div class="ui form" style="margin-bottom: 2.5vh;">
        <h1 class="ui dividing header">Submission Form</h1>
        <div class="fields">
            <div class="sixteen wide field">
                <div class="row">
                <span>
                    <!-- <i data-tooltip="Add users to your feed" class="question circle icon"></i> -->
                    <label class="">
                        <i class="pop-up question blue circle icon"
                           data-title="A URL from your github repo to a specific file"
                           data-content="Ex: https://github.com/Tthomas63/chagrade_test_submission/blob/master/chagrade_test_submission-master.zip"></i>
                        Github Submission:
                    </label>
                </span>
                </div>
                <div class="ui horizontal divider"></div>
                <div class="row">
                    <div class="ui search selection dropdown repository" ref="github_repo">
                        <!--<div class="default text">Repository</div>-->
                        <div class="default text">{ submission.github_repo_name}</div>
                        <i class="dropdown icon"></i>
                        <div class="menu">
                            <div each="{repository, r in github_repositories}" class="item" data-value="{r}" data-text="{ repository.name }">{ repository.name }</div>
                        </div>
                    </div>
                    <div class="ui search selection dropdown branch" ref="github_branch">
                        <!--<div class="default text">Branch</div>-->
                        <div class="default text">{ submission.github_branch_name}</div>
                        <i class="dropdown icon"></i>
                        <div class="menu">
                            <div each="{branch in github_branches}" class="item" data-text="{ branch.name }">{ branch.name }</div>
                        </div>
                    </div>
                </div>
                <div class="ui horizontal divider"></div>
                <div class="sixteen wide row">
                    <div class="ui search selection dropdown commit" ref="github_commit_hash">
                        <!--<div class="default text">Commit</div>-->
                        <i class="dropdown icon"></i>
                        <div class="default text">{ submission.github_commit_hash}</div>
                        <div class="menu">
                            <div each="{commit in github_commits}" class="item" data-text="{ commit.sha }">
                                <div class="ui container"
                                    <div class="ui row">
                                        <div class="commit-header">
                                            <div class='sha'>
                                                { commit.sha.slice(0,8) }
                                            </div>
                                            <div class='commit-message'>
                                                { commit.commit.message }
                                            </div>
                                        </div>
                                    </div>
                                    <div class="ui horizontal divider"></div>
                                    <div class="ui row">
                                        <div class='commit-date'>
                                            { commit.commit.committer.date.slice(0,10) }
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="fields">
            <div show="{definition.ask_method_name}" class="four wide field">
                <label>
                    Method Name:
                </label>
                <input required name="method_name" ref="method_name" type="text" value="{submission.method_name || ''}">
            </div>
            <div show="{definition.ask_method_description}" class="four wide field">
                <label>
                    Method Description:
                </label>
                <input required name="method_description" ref="method_description" type="text"
                       value="{submission.method_description || ''}">
            </div>
            <div show="{definition.ask_project_url}" class="four wide field">
                <label>
                    Project URL:
                </label>
                <input required name="project_url" ref="project_url" type="text" value="{submission.project_url || ''}">
            </div>
            <div show="{definition.ask_publication_url}" class="four wide field">
                <label>
                    Publication URL:
                </label>
                <input name="publication_url" ref="publication_url" type="text"
                       value="{submission.publication_url || ''}">
            </div>
        </div>
        <h2 class="ui dividing header">Extra Questions:</h2>
        <div each="{question, index in definition.custom_questions}" class="fields">
            <div class="sixteen wide field">
                <input name="{'question_id_' + index}" ref="{'question_id_' + index}" type="hidden"
                       value="{question.id}">
                <label>{question.question}:</label>
                <input data-question-id="" name="{'question_answer_' + index}" ref="{'question_answer_' + index}"
                       type="text" value="{question.prev_answer || ''}">
            </div>
        </div>
    </div>

    <span><a onclick="{submit_form}" class="ui green button">Submit</a><a onclick="{cancel_button}"
                                                                          class="ui red button">Cancel</a></span>

    <script>


        var self = this
        self.errors = []
        self.question_answers = []
        self.definition = {
            'ask_publication_url': false,
            'ask_project_url': false,
            'ask_method_name': false,
            'ask_method_description': false,
        }
        self.submission = {
            'method_name': '',
            'method_description': '',
            'project_url': '',
            'publication_url': '',
            'github_url': '',
            'github_repo_name': '',
            'github_branch_name': '',
            'github_commit_hash': '',
        }

        self.one('mount', function () {
            self.update_definition()

            $('.pop-up').popup({
                inline: true,
                position: 'top left',
            });
            $('.ui.dropdown.repository', self.root).dropdown({
                onChange: function(value, text, $selectedItem) {
                    self.github_repo = self.github_repositories[parseInt(value)]
                    $.ajax({
                        type: 'GET',
                        url: self.github_repo.branches_url.split('{')[0],
                        data: JSON.stringify(null),
                        headers:{"Authorization": 'token ' + self.github_information.access_token},
                        contentType: "application/json",
                        dataType: 'json'
                    })
                    .done(function (branch_data) {
                        console.log('branch_data')
                        console.log(branch_data)
                        self.github_branches = branch_data
                        self.update()
                    })
                    $.ajax({
                        type: 'GET',
                        url: self.github_repo.commits_url.split('{')[0],
                        data: JSON.stringify(null),
                        headers:{"Authorization": 'token ' + self.github_information.access_token},
                        contentType: "application/json",
                        dataType: 'json'
                    })
                    .done(function (commit_data) {
                        console.log('commit_data')
                        console.log(commit_data)
                        self.github_commits = commit_data
                        self.update()
                    })
                    $('.ui.dropdown.branch', self.root).dropdown('restore defaults')
                    $('.ui.dropdown.commit', self.root).dropdown('restore defaults')
                }
            })
            $('.ui.dropdown.branch', self.root).dropdown({
            })
            $('.ui.dropdown.commit', self.root).dropdown({
            })
        })



        self.submit_form = function () {

            if (window.SUBMISSION !== undefined) {
                var result = confirm("There is already an existing submission. Submitting again will overwrite the previous submission and any previously attached grades will be lost. Continue?")
                if (!result) {
                    return
                }
            }

            var data = {
                "klass": KLASS,
                "definition": DEFINITION,
                "creator": STUDENT,
                "github_url": 'https://github.com/Tthomas63/chagrade_test_submission/blob/master/chagrade_test_submission-master.zip', //self.refs.github_url,
                "github_repo_name": $(self.refs.github_repo).dropdown('get text'),
                "github_branch_name": $(self.refs.github_branch).dropdown('get text'),
                "github_commit_hash": $(self.refs.github_commit_hash).dropdown('get text'),
                "method_name": self.refs.method_name.value || '',
                "method_description": self.refs.method_description.value || '',
                "project_url": self.refs.project_url.value || '',
                "publication_url": self.refs.publication_url.value || '',
                "question_answers": [
                    /*{
                     "question": 0,
                     "text": "string"
                     }*/
                ]
            }

            console.log('post data')
            console.log(data)

            if (window.USER_TEAM !== undefined) {
                data['team'] = window.USER_TEAM
            }

            for (var index = 0; index < self.definition.custom_questions.length; index++) {
                var temp_data = {
                    'question': self.refs['question_id_' + index].value,
                    'text': self.refs['question_answer_' + index].value
                }
                data['question_answers'].push(temp_data)

            }

            CHAGRADE.api.create_submission(data)
                .done(function (data) {
                    window.location = '/homework/overview/' + KLASS
                })
                .fail(function (response) {
                    Object.keys(response.responseJSON).forEach(function (key) {
                        if (key === 'question_answers') {
                            toastr.error("An error occured with " + key + "! Please make sure you did not leave any fields blank.")
                        } else {
                            toastr.error("Error with " + key + "! " + response.responseJSON[key])
                        }
                    });
                })
        }

        self.update_question_answers = function () {
            var data = self.definition

            for (var index = 0; index < self.submission.question_answers.length; index++) {
                for (var question_index = 0; question_index < data.custom_questions.length; question_index++) {
                    if (self.submission.question_answers[index].question === data.custom_questions[question_index].id) {
                        data.custom_questions[question_index].prev_answer = self.submission.question_answers[index].text
                        data.custom_questions[question_index].answer_id = self.submission.question_answers[index].id
                    }
                }
            }
            self.update({definition: data})
        }

        self.update_submission = function () {
            CHAGRADE.api.get_submission(SUBMISSION)
                .done(function (data) {
                    self.submission = data
                    console.log('submission')
                    console.log(data)
                    self.update()
                    self.update_question_answers()
                })
                .fail(function (error) {
                    toastr.error("Error fetching submission: " + error.statusText)
                })
        }

        self.cancel_button = function () {
            window.location = '/homework/overview/' + KLASS
        }

        self.update_definition = function () {
            CHAGRADE.api.get_definition(DEFINITION)
                .done(function (data) {
                        self.definition = data
                        self.update()
                })
                .fail(function (error) {
                    toastr.error("Error fetching definition: " + error.statusText)
                })

            CHAGRADE.api.get_cha_user(self.opts.pk)
                .done(function (data) {
                    console.log(data)
                    self.github_information = data.github_info

                    $.ajax({
                        type: 'GET',
                        url: self.github_information.repos_url,
                        data: JSON.stringify(null),
                        headers:{"Authorization": 'token ' + self.github_information.access_token},
                        contentType: "application/json",
                        dataType: 'json'
                    })
                    .done(function (repo_data) {
                        console.log('repo_data')
                        console.log(repo_data)
                        self.github_repositories = repo_data
                        self.update()
                    })
                })
                .fail(function (error) {
                    toastr.error("Error fetching user: " + error.statusText)
                })


            if (window.SUBMISSION !== undefined) {
                self.update_submission()
            }
        }
    </script>
</submit-homework-github>