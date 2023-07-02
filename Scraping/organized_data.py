def cleaningDataset(df):
    df[["user_name", "userid", "tweet_time_stamp"]] = df['tweet_used'].str.split('\n', n=2, expand=True)
    df['userid'] = df['userid'].str.replace("@", "")


def final_merge(df1, df2):
    merged_df = df1.merge(df2, on='userid', how='left')
    today = date.today()
    merged_df.drop_duplicates(['tweet_link'], inplace=True)
    merged_df.to_csv(f"tweets_scraped_{today}.csv", index=False)


def looking_for_missing(df1, df2):
    df1[["user_name", "userid", "tweet_time_stamp"]] = df1['tweet_used'].str.split('\n', n=2, expand=True)
    df1['userid'] = df1['userid'].str.replace("@", "")
    df3 = df1.merge(df2, on='userid', how='outer', indicator=True)
    df3 = df3[df3['_merge'] == 'left_only']
    df3.to_csv("missing_profiles.csv", index=False)


def get_missing_profiles(driver):
    df1 = pd.read_csv("tweet_scraped.csv")
    df2 = pd.read_csv("the_tweets_user_bio.csv")
    looking_for_missing(df1, df2)
    df3 = pd.read_csv("missing_profiles.csv")
    df3[["user_name", "userid", "tweet_time_stamp"]] = df3['tweet_used'].str.split('\n', n=2, expand=True)
    df3['userid'] = df3['userid'].str.replace("@", "")
    get_user_profile_info_to_csv(df3, driver, 0)


def get_user_profile_info_to_csv(df, driver, last_index):
    user_url_df = get_new_user_url(df)
    user_url_df = user_url_df[last_index:]
    get_data_from_new_url(user_url_df, driver)


def merge_missing(df1, df2):
    merged_df_profile_bio = pd.concat([df1, df2])
    merged_df_profile_bio = merged_df.reset_index(drop=True)
    merged_df_profile_bio.to_csv("the_tweets_user_bio.csv", index=False)
