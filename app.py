from flask import Flask, render_template
# import os
# import ldclient
# from ldclient.config import Config
# from ldclient import Context

# # Initialize LaunchDarkly client & context
# ldclient.set_config(Config(os.getenv("LD_SDK_KEY")))
# ld_client = ldclient.get()
# context = Context.builder("context-key-123abc").name("Sandy").build()

app = Flask(__name__)

@app.route("/")
def landing_page():
    # # Evaluate the feature flag
    # show_next = ld_client.variation("dojo-release-landing-page", context, False)
    # if show_next:
    #     return render_template("landing_next.html")
    # else:
    #     return render_template("landing.html")
    return render_template("landing.html")

if __name__ == "__main__":
    app.run(debug=True)