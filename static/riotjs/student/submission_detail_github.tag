<submission-detail-github>

<!--    <div class="ui grid"> -->
<!--        <div class="six wide column"> -->
<!--            <p>Date: { format_date(submission.created) }</p> -->
<!--            <p if={ submission.commit_hash && submission.commit_hash != "Commit" }>Commit hash: { submission.commit_hash.slice(0,6) }</p> -->
<!--            <a class="ui tiny black button" href="{ submission.github_url }">Submission File</a> -->
<!--            <p if={ submission.github_repo_name }>Repository Name: { submission.github_repo_name }</p> -->
<!--            <p if={ submission.github_branch_name && submission.github_branch_name != "Branch"}>Branch Name: { submission.github_branch_name }</p> -->
<!--            <div class="ui relaxed celled list"> -->
<!--                <ol> -->
<!-- -->
<!--                    {% for answer in submission.question_answers.all %} -->
<!--                        <li each="answer in submission.question_answers">{{ answer.question.question }}: {{ answer.text }}</li> -->
<!--                    {% endfor %} -->
<!--                </ol> -->
<!--            </div> -->
<!--        </div> -->
<!--        <div class="ten wide column"> -->
            <div class="ui header">
                Repository Activity
            </div>

            <div class="commit-container">
                <div each={commit in commits} class="ui grid commit">
                    <div class="row commit-header">
                        <a class="ui blue label" href="{ commit.html_url }">
                            <i class="hashtag icon"></i>
                            {commit.sha.slice(0,6)}
                        </a>
                        <a class="ui right floated author" href="{ commit.author.html_url }">
                            { commit.commit.author.name }
                        </a>
                        <br>
                        <div class="date">
                            {format_date(commit.commit.committer.date)}
                        </div>
                    </div>
                    <div class="ui row commit-message">
                        {commit.commit.message}
                    </div>
                </div>
            </div>
<!--        </div> -->
<!--    </div> -->
<!--    </div> -->
    <script>
        var self = this
        self.errors = []
        self.submission = {}

        self.github_requests = 0

        var datetime = luxon.DateTime

        self.one('mount', function () {
            self.update_submission()
        })

        self.github_request = (url, done_function) => {
            $.ajax({
                type: 'GET',
                url: url,
                data: JSON.stringify(null),
                headers:{"Authorization": 'token ' + self.github_information.access_token},
                contentType: "application/json",
                dataType: 'json',
            })
            .done(done_function)
            .fail(function (error) {
                toastr.error("Github API Error: " + error.statusText)
            })
        }

        self.format_date = function (iso_string) {
            let d = datetime.fromISO(iso_string)
            return d.toRelative()
        }

        self.cancel_button = function () {
            window.location = '/homework/overview/' + KLASS
        }

        self.update_submission = function () {
            CHAGRADE.api.get_submission(self.opts.submission_pk)
                .done(function (data) {
                    console.log('Submission Data')
                    console.log(data)
                    console.log('Submission Data')
                    self.submission = data
                    if (!!self.submission.github_commit_hash) {
                        self.github_ref = self.submission.github_commit_hash
                    } else if (!!self.submission.github_branch_name) {
                        self.github_ref = self.submission.github_branch_name
                    } else {
                        self.github_ref = null
                    }
                    self.update()
                    CHAGRADE.api.get_cha_user(self.opts.user_pk)
                        .done(function (data) {
                            self.github_information = data.github_info
                            self.user_information = data
                            self.github_request(self.github_information.repos_url, function (repo_data) {
                                self.github_repositories = repo_data
                                let repo = _.find(repo_data, ['name', self.submission.github_repo_name])
                                self.github_request(repo.commits_url.split('{')[0], function (data) {
                                    self.commits = data
                                    console.log(data)
                                    self.update()
                                })
                                self.update()
                            })
                        })
                        .fail(function (error) {
                            toastr.error("Error fetching user: " + error.statusText)
                        })
                })
                .fail(function (error) {
                    toastr.error("Error fetching submission: " + error.statusText)
                })

        }
    </script>
    <style>
        .ten.wide.column {
            height: 100%;
        }

        .commit {
            margin: 28px 0 28px 0 !important;
            font-size: 1.3em;
            line-height: 1.5em;
        }

        .commit-container {
            height: 40vh;
            overflow-y: scroll;
        }

        .commit-header {
            padding-bottom: 10px !important;
        }

        .commit-message {
            padding-top: 0 !important;
            font-size: 0.8em;
        }

        .author {
            color: #444444;
            margin-left: 15px;
            margin-right: auto;
        }

        .date {
            color: #888888;
            margin-right: 15px;
            font-size: 0.8em;
        }
    </style>
</submission-detail-github>
