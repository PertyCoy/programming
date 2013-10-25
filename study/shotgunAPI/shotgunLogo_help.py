from shotgun_api3 import Shotgun
'''
#sample
help(sg)
Help on Shotgun in module shotgun_api3.shotgun object:

class Shotgun(__builtin__.object)
 |  Shotgun Client Connection
 |  
 |  Methods defined here:
 |  
 |  __init__(self, base_url, script_name, api_key, convert_datetimes_to_utc=True, http_proxy=None, ensure_ascii=True, connect=True, ca_certs=None)
 |      Initialises a new instance of the Shotgun client.
 |      
 |      :param base_url: http or https url to the shotgun server.
 |      
 |      :param script_name: name of the client script, used to authenticate
 |      to the server.
 |      
 |      :param api_key: key assigned to the client script, used to
 |      authenticate to the server.
 |      
 |      :param convert_datetimes_to_utc: If True date time values are
 |      converted from local time to UTC time before been sent to the server.
 |      Datetimes received from the server are converted back to local time.
 |      If False the client should use UTC date time values.
 |      Default is True.
 |      
 |      :param http_proxy: Optional, URL for the http proxy server, on the
 |      form [username:pass@]proxy.com[:8080]
 |      
 |      :param connect: If True, connect to the server. Only used for testing.
 |              
 |              :param ca_certs: The path to the SSL certificate file. Useful for users
 |              who would like to package their application into an executable.
 |  
 |  add_user_agent(self, agent)
 |      Add agent to the user-agent header
 |      
 |      Append agent to the string passed in as the user-agent to be logged
 |      in events for this API session.
 |      
 |      :param agent: Required, string to append to user-agent.
 |  
 |  authenticate_human_user(self, user_login, user_password)
 |      Authenticate Shotgun HumanUser. HumanUser must be an active account.
 |      @param user_login: Login name of Shotgun HumanUser
 |      @param user_password: Password for Shotgun HumanUser
 |      @return: Dictionary of HumanUser including ID if authenticated, None is unauthorized.
 |  
 |  batch(self, requests)
 |      Make a batch request  of several create, update and delete calls.
 |      
 |      All requests are performed within a transaction, so either all will
 |      complete or none will.
 |      
 |      :param requests: A list of dict's of the form which have a
 |          request_type key and also specifies:
 |          - create: entity_type, data dict of fields to set
 |          - update: entity_type, entity_id, data dict of fields to set
 |          - delete: entity_type and entity_id
 |      
 |      :returns: A list of values for each operation, create and update
 |      requests return a dict of the fields updated. Delete requests
 |      return True if the entity was deleted.
 |  
 |  close(self)
 |      Closes the current connection to the server.
 |      
 |      If the client needs to connect again it will do so automatically.
 |  
 |  connect(self)
 |      Forces the client to connect to the server if it is not already
 |      connected.
 |      
 |      NOTE: The client will automatically connect to the server. Only
 |      call this function if you wish to confirm the client can connect.
 |  
 |  create(self, entity_type, data, return_fields=None)
 |      Create a new entity of the specified entity_type.
 |      
 |      :param entity_type: Required, entity type (string) to create.
 |      
 |      :param data: Required, dict fields to set on the new entity.
 |      
 |      :param return_fields: Optional list of fields from the new entity
 |      to return. Defaults to 'id' field.
 |      
 |      :returns: dict of the requested fields.
 |  
 |  delete(self, entity_type, entity_id)
 |      Retire the specified entity.
 |      
 |      The entity can be brought back to life using the revive function.
 |      
 |      :param entity_type: Required, entity type (string) to delete.
 |      
 |      :param entity_id: Required, id of the entity to delete.
 |      
 |      :returns: True if the entity was deleted, False otherwise e.g. if the
 |      entity has previously been deleted.
 |  
 |  download_attachment(self, attachment=False, file_path=None, attachment_id=None)
 |      Downloads the file associated with a Shotgun Attachment.
 |      
 |      NOTE: On older (< v5.1.0) Shotgun versions, non-downloadable files 
 |      on Shotgun don't raise exceptions, they cause a server error which 
 |      returns a 200 with the page content.
 |      
 |      :param attachment: (mixed) Usually a dict representing an Attachment.
 |      The dict should have a 'url' key that specifies the download url. 
 |      Optionally, the dict can be a standard entity hash format with 'id' and
 |      'type' keys as long as 'type'=='Attachment'. This is only supported for
 |      backwards compatibility (#22150).
 |      If an int value is passed in, the Attachment with the matching id will
 |      be downloaded from the Shotgun server.
 |      
 |      :param file_path: (str) Optional. If provided, write the data directly
 |      to local disk using the file_path. This avoids loading all of the data 
 |      in memory and saves the file locally which is probably what is desired
 |      anyway. 
 |      
 |      :param attachment_id: (int) Optional. Deprecated in favor of passing in 
 |      Attachment hash to attachment param. This attachment_id exists only for
 |      backwards compatibility for scripts specifying the parameter with
 |      keywords.
 |      
 |      :returns: (str) If file_path is None, returns data of the Attachment 
 |      file as a string. If file_path is provided, returns file_path.
 |  
 |  entity_types(self)
 |  
 |  find(self, entity_type, filters, fields=None, order=None, filter_operator=None, limit=0, retired_only=False, page=0)
 |      Find entities matching the given filters.
 |      
 |      :param entity_type: Required, entity type (string) to find.
 |      
 |      :param filters: Required, list of filters to apply.
 |      
 |      :param fields: Optional list of fields from the matched entities to
 |      return. Defaults to id.
 |      
 |      :param order: Optional list of fields to order the results by, list
 |      has the form [{'field_name':'foo','direction':'asc or desc'},]
 |      
 |      :param filter_operator: Optional operator to apply to the filters,
 |      supported values are 'all' and 'any'. Defaults to 'all'.
 |      
 |      :param limit: Optional, number of entities to return per page.
 |      Defaults to 0 which returns all entities that match.
 |      
 |      :param page: Optional, page of results to return. By default all
 |      results are returned. Use together with limit.
 |      
 |      :param retired_only: Optional, flag to return only entities that have
 |      been retried. Defaults to False which returns only entities which
 |      have not been retired.
 |      
 |      :returns: list of the dicts for each entity with the requested fields,
 |      and their id and type.
 |  
 |  find_one(self, entity_type, filters, fields=None, order=None, filter_operator=None, retired_only=False)
 |      Calls the find() method and returns the first result, or None.
 |      
 |      :param entity_type: Required, entity type (string) to find.
 |      
 |      :param filters: Required, list of filters to apply.
 |      
 |      :param fields: Optional list of fields from the matched entities to
 |      return. Defaults to id.
 |      
 |      :param order: Optional list of fields to order the results by, list
 |      has the form [{'field_name':'foo','direction':'asc or desc'},]
 |      
 |      :param filter_operator: Optional operator to apply to the filters,
 |      supported values are 'all' and 'any'. Defaults to 'all'.
 |      
 |      :param limit: Optional, number of entities to return per page.
 |      Defaults to 0 which returns all entities that match.
 |      
 |      :param page: Optional, page of results to return. By default all
 |      results are returned. Use together with limit.
 |      
 |      :param retired_only: Optional, flag to return only entities that have
 |      been retried. Defaults to False which returns only entities which
 |      have not been retired.
 |  
 |  follow(self, user, entity)
 |      Adds the entity to the user's followed entities (or does nothing if the user is already following the entity)
 |      
 |      :param dict user: User entity to follow the entity
 |      :param dict entity: Entity to be followed
 |      
 |      :returns: dict with 'followed'=true, and dicts for the 'user' and 'entity' that were passed in
 |  
 |  followers(self, entity)
 |      Gets all followers of the entity.
 |      
 |      :param dict entity: Find all followers of this entity
 |      
 |      :returns list of dicts for all the users following the entity
 |  
 |  get_attachment_download_url(self, attachment)
 |      Returns the URL for downloading provided Attachment.
 |      
 |      :param attachment: (mixed) If type is an int, construct url to download
 |      Attachment with id from Shotgun. 
 |      If type is a dict, and a url key is present, use that url. 
 |      If type is a dict, and url key is not present, check if we have
 |      an id and type keys and the type is 'Attachment' in which case we 
 |      construct url to download Attachment with id from Shotgun as if just
 |      the id has been passed in. 
 |      
 |      :todo: Support for a standard entity hash should be removed: #22150
 |      
 |      :returns: (str) the download URL for the Attachment or None if None was
 |      passed to attachment param. This avoids raising an error when results
 |      from a find() are passed off to a download_attachment() call.
 |  
 |  info(self)
 |      Calls the Info function on the Shotgun API to get the server meta.
 |      
 |      :returns: dict of the server meta data.
 |  
 |  reset_user_agent(self)
 |      Reset user agent to the default
 |  
 |  revive(self, entity_type, entity_id)
 |      Revive an entity that has previously been deleted.
 |      
 |      :param entity_type: Required, entity type (string) to revive.
 |      
 |      :param entity_id: Required, id of the entity to revive.
 |      
 |      :returns: True if the entity was revived, False otherwise e.g. if the
 |      entity has previously been revived (or was not deleted).
 |  
 |  schema(self, entity_type)
 |      # Deprecated methods from old wrapper
 |  
 |  schema_entity_read(self)
 |      Gets all active entities defined in the schema.
 |      
 |      :returns: dict of Entity Type to dict containing the display name.
 |  
 |  schema_field_create(self, entity_type, data_type, display_name, properties=None)
 |      Creates a field for the specified entity type.
 |      
 |      :param entity_type: Required, entity type (string) to add the field to
 |      
 |      :param data_type: Required, Shotgun data type for the new field.
 |      
 |      :param display_name: Required, display name for the new field.
 |      
 |      :param properties: Optional, dict of properties for the new field.
 |      
 |      :returns: The Shotgun name (string) for the new field, this is
 |      different to the display_name passed in.
 |  
 |  schema_field_delete(self, entity_type, field_name)
 |      Deletes the specified field definition from the entity_type.
 |      
 |      :param entity_type: Required, entity type (string) to delete the field
 |      from.
 |      
 |      :param field_name: Required, Shotgun name of the field to delete.
 |      
 |      :param properties: Required, dict of updated properties for the field.
 |      
 |      :returns: True if the field was updated, False otherwise.
 |  
 |  schema_field_read(self, entity_type, field_name=None)
 |      Gets all schema for fields in the specified entity_type or one
 |      field.
 |      
 |      :param entity_type: Required, entity type (string) to get the schema
 |      for.
 |      
 |      :param field_name: Optional, name of the field to get the schema
 |      definition for. If not supplied all fields for the entity type are
 |      returned.
 |      
 |      :returns: dict of field name to nested dicts which describe the field
 |  
 |  schema_field_update(self, entity_type, field_name, properties)
 |      Updates the specified field definition with the supplied
 |      properties.
 |      
 |      :param entity_type: Required, entity type (string) to add the field to
 |      
 |      :param field_name: Required, Shotgun name of the field to update.
 |      
 |      :param properties: Required, dict of updated properties for the field.
 |      
 |      :returns: True if the field was updated, False otherwise.
 |  
 |  schema_read(self)
 |      Gets the schema for all fields in all entities.
 |      
 |      :returns: nested dicts
 |  
 |  set_session_uuid(self, session_uuid)
 |      Sets the browser session_uuid for this API session.
 |      
 |      Once set events generated by this API session will include the
 |      session_uuid in their EventLogEntries.
 |      
 |      :param session_uuid: Session UUID to set.
 |  
 |  set_up_auth_cookie(self)
 |      Sets up urllib2 with a cookie for authentication on the Shotgun 
 |      instance.
 |  
 |  share_thumbnail(self, entities, thumbnail_path=None, source_entity=None, filmstrip_thumbnail=False, **kwargs)
 |  
 |  summarize(self, entity_type, filters, summary_fields, filter_operator=None, grouping=None)
 |      Return group and summary information for entity_type for summary_fields
 |      based on the given filters.
 |  
 |  unfollow(self, user, entity)
 |      Removes entity from the user's followed entities (or does nothing if the user is not following the entity)
 |      
 |      :param dict user: User entity to unfollow the entity
 |      :param dict entity: Entity to be unfollowed
 |      
 |      :returns: dict with 'unfollowed'=true, and dicts for the 'user' and 'entity' that were passed in
 |  
 |  update(self, entity_type, entity_id, data)
 |      Updates the specified entity with the supplied data.
 |      
 |      :param entity_type: Required, entity type (string) to update.
 |      
 |      :param entity_id: Required, id of the entity to update.
 |      
 |      :param data: Required, dict fields to update on the entity.
 |      
 |      :returns: dict of the fields updated, with the entity_type and
 |      id added.
 |  
 |  upload(self, entity_type, entity_id, path, field_name=None, display_name=None, tag_list=None)
 |      Upload a file as an attachment/thumbnail to the specified
 |      entity_type and entity_id.
 |      
 |      :param entity_type: Required, entity type (string) to revive.
 |      
 |      :param entity_id: Required, id of the entity to revive.
 |      
 |      :param path: path to file on disk
 |      
 |      :param field_name: the field on the entity to upload to
 |          (ignored if thumbnail)
 |      
 |      :param display_name: the display name to use for the file in the ui
 |          (ignored if thumbnail)
 |      
 |      :param tag_list: comma-separated string of tags to assign to the file
 |      
 |      :returns: Id of the new attachment.
 |  
 |  upload_filmstrip_thumbnail(self, entity_type, entity_id, path, **kwargs)
 |      Convenience function for uploading thumbnails, see upload.
 |  
 |  upload_thumbnail(self, entity_type, entity_id, path, **kwargs)
 |      Convenience function for uploading thumbnails, see upload.
 |  
 |  work_schedule_read(self, start_date, end_date, project=None, user=None)
 |      Get the work day rules for a given date range.
 |      
 |      reasons:
 |          STUDIO_WORK_WEEK
 |          STUDIO_EXCEPTION
 |          PROJECT_WORK_WEEK
 |          PROJECT_EXCEPTION
 |          USER_WORK_WEEK
 |          USER_EXCEPTION
 |      
 |      
 |      :param start_date: Start date of date range.
 |      :type start_date: str (YYYY-MM-DD)
 |      :param end_date: End date of date range.
 |      :type end_date: str (YYYY-MM-DD)
 |      :param dict project: Project entity to query WorkDayRules for. (optional)
 |      :param dict user: User entity to query WorkDayRules for. (optional)
 |  
 |  work_schedule_update(self, date, working, description=None, project=None, user=None, recalculate_field=None)
 |      Update the work schedule for a given date. If neither project nor user are passed the studio work schedule will be updated.
 |      Project and User can only be used separately.
 |      
 |      :param date: Date of WorkDayRule to update.
 |      :type date: str (YYYY-MM-DD)
 |      :param bool working:
 |      :param str description: Reason for time off. (optional)
 |      :param dict project: Project entity to assign to. Cannot be used with user. (optional)
 |      :param dict user: User entity to assign to. Cannot be used with project. (optional)
 |      :param str recalculate_field: Choose the schedule field that will be recalculated on Tasks when they are affected by a change in working schedule. 'due_date' or 'duration', default is a Site Preference (optional)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  server_caps
 |      :returns: ServerCapabilities that describe the server the client is
 |      connected to.
 |  
 |  server_info
 |      Returns server information.
 '''